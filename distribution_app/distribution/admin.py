from django.contrib import admin

from distribution.models import Settings, Message, Logs, Status, Interval


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'distribution_time', 'distribution_periodicity', 'distribution_status',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'owner',)
    search_fields = ('subject',)


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'last_attempt_time', 'last_attempt_status', 'last_attempt_response',)
    list_filter = ('last_attempt_time',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status',)


@admin.register(Interval)
class IntervalAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time_interval',)

