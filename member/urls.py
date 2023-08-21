from django.urls import path
from django.views.generic import TemplateView

from member.views import LoginView, MyPageView

app_name = 'member'

urlpatterns = [
    path('login/', TemplateView.as_view(template_name='header/header.html'), name='login'),
    # path('mypage/', MyPageView.as_view('mypage/mypage-profile.html'), name='mypage'),
    path('oauth/redirect', LoginView.as_view(), name='redirect')
]