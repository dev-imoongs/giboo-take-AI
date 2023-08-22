from django.urls import path
from django.views.generic import TemplateView

from main.views import MainView
from member.views import LoginView, LogoutView

app_name = 'member'

urlpatterns = [
    path('login/', LoginView.as_view(), name='redirect'),
    path('logout/', LogoutView.as_view(), name='logout'),
]