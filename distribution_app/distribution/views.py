import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Post
from distribution.forms import *
from distribution.models import *
from services.crontask.crontask_job import crontab_job
from users.models import User


class GetContextMixin:

    def form_valid(self, form):
        formset = self.get_context_data()['settings_formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_context_data(self, **kwargs):

        if settings.CACHE_ENABLED:
            key = 'user_list'
            user_list = cache.get(key)
            if user_list is None:
                user_list = User.objects.all()
                cache.set(key, user_list)
        else:
            user_list = User.objects.all()

        context_data = super().get_context_data()
        setting_list = Settings.objects.all()
        context_data['settings_list'] = setting_list
        crontab_job(context_data)
        posts_pk_list: list = list(Post.objects.values_list('pk', flat=True))
        random.shuffle(posts_pk_list)
        parameters = {
            'settings_count': str(len(Settings.objects.all())),
            'active_settings_count': str(
                len(Settings.objects.filter(distribution_status=Status.objects.get(status='started')))),
            'users_count': str(len(user_list)),
            'random_posts': [Post.objects.get(pk=posts_pk_list[i]) for i in range(len(posts_pk_list))][:3]
        }
        context_data['parameters'] = parameters
        return context_data


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        # Добавляем Settings
        setting = Settings.objects.get(message=context_data['object'].pk)
        context_data['setting'] = setting
        # Добавляем Logs
        logs_list = Logs.objects.filter(message=context_data['object'].pk)
        context_data['logs_list'] = logs_list
        return context_data


class MessageCreateView(LoginRequiredMixin, GetContextMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('distribution:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        # Добавляем Settings
        SettingsFormset = inlineformset_factory(Message, Settings, form=SettingsForm, extra=1)
        if self.request.method == 'POST':
            context_data['settings_formset'] = SettingsFormset(self.request.POST, instance=self.object)
        else:
            context_data['settings_formset'] = SettingsFormset(instance=self.object)
        return context_data


class MessageUpdateView(LoginRequiredMixin, GetContextMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('distribution:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        # Добавляем Settings
        SettingsFormset = inlineformset_factory(Message, Settings, form=SettingsForm, extra=0)
        if self.request.method == 'POST':
            formset = SettingsFormset(self.request.POST, instance=self.object)
            if formset.is_valid():
                for form in formset.forms:
                    if form.cleaned_data.get('distribution_start_time'):
                        form.instance.distribution_start_time = form.cleaned_data['distribution_start_time']
                formset.save()
            context_data['settings_formset'] = formset
        else:
            context_data['settings_formset'] = SettingsFormset(instance=self.object)
        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and self.request.user.is_staff is not True:
            raise Http404
        return self.object


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('distribution:home')


def change_status(request, message_pk):
    message_settings = get_object_or_404(Settings, message=message_pk)
    if message_settings.distribution_status.status == 'started':
        new_status = 'completed'
    else:
        new_status = 'started'
    message_settings.distribution_status = Status.objects.get(status=new_status)
    message_settings.save()
    return redirect('distribution:home')
