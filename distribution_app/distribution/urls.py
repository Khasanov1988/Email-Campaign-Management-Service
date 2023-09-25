from django.urls import path
from distribution import views
from distribution.apps import DistributionConfig
from distribution.views import MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView, \
    MessageCreateView

app_name = DistributionConfig.name

urlpatterns = [
    path('', MessageListView.as_view(), name='home'),  # Home page displaying a list of messages
    path('view/<int:pk>', MessageDetailView.as_view(), name='view'),  # View details of a specific message
    path('edit/<int:pk>/', MessageUpdateView.as_view(), name='edit'),  # Edit a specific message
    path('delete/<int:pk>/', MessageDeleteView.as_view(), name='delete'),  # Delete a specific message
    path('create/', MessageCreateView.as_view(), name='create'),  # Create a new message
    path('change_status/<int:message_pk>/', views.change_status, name='change_status'), # Change the status of a message
]
