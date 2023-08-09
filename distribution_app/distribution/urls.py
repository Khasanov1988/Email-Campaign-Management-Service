from django.urls import path

from distribution import views
from distribution.apps import DistributionConfig

from distribution.views import MessageListView, MessageDetailView, MessageUpdateView, \
    MessageDeleteView, MessageCreateView

app_name = DistributionConfig.name

urlpatterns = [
    path('', MessageListView.as_view(), name='home'),
    path('view/<int:pk>', MessageDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', MessageUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MessageDeleteView.as_view(), name='delete'),
    path('create/', MessageCreateView.as_view(), name='create'),
    path('change_status/<int:message_pk>/', views.change_status, name='change_status'),
]
