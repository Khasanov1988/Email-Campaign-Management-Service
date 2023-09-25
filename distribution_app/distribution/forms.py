from django import forms
from django.forms import BooleanField
from distribution.models import *


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-control'


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'text',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['subject']

        for name in cleaned_data.strip().split():
            if name.lower() in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                                'радар']:
                raise forms.ValidationError('You are trying to create a prohibited message')

        return cleaned_data


class SettingsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Settings
        exclude = ('owner',)


class LogsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Logs
        fields = '__all__'
