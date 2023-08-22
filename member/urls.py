from django.urls import path
from django.views.generic import TemplateView

from main.views import MainView
from member.views import LoginView, LoginedView, LogoutView

app_name = 'member'

urlpatterns = [
    path('login/', TemplateView.as_view(template_name='header/header.html'), name='login'),
    path('logined/', LoginedView.as_view(), name='logined'),
    path('oauth/redirect', LoginView.as_view(), name='redirect'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logined/reset/', TemplateView.as_view(template_name='header/header.html'), name='reset')
]