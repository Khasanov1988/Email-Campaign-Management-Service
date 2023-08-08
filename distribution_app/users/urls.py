from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


from users.views import RegisterView, ProfileView, LoginModifiedView, generate_new_password

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginModifiedView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/genpassword', generate_new_password, name='generate_new_password'),
]