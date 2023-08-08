from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from distribution.forms import *
from distribution.models import *


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

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if not self.request.user.is_staff:
    #         queryset = queryset.filter(
    #             is_published=True,
    #         )
    #
    #     return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        version_list = Settings.objects.all()
        context_data['formset'] = version_list
        return context_data


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        # Добавляем Settings
        SettingsFormset = inlineformset_factory(Message, Settings, form=SettingsForm, extra=0)
        context_data['settings_formset'] = SettingsFormset(instance=self.object)
        # Добавляем Logs
        LogsFormset = inlineformset_factory(Message, Logs, form=LogsForm, extra=0)
        context_data['logs_formset'] = LogsFormset(instance=self.object)
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
            context_data['settings_formset'] = SettingsFormset(self.request.POST, instance=self.object)
        else:
            context_data['settings_formset'] = SettingsFormset(instance=self.object)
        return context_data


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('distribution:home')


