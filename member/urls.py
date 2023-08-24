from django.urls import path
from member.views import LoginView, LogoutView, LoginAPIView

app_name = 'member'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # api view
    path('reset/', LoginAPIView.as_view(), name='reset')
]