from django.urls import path
from member.views import LoginView, LogoutView, LoginAPIView, GetMemberProfileAPIView, GetMemberAlarmsNotChckedAPIView


app_name = 'member'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('callback/', LoginView.as_view(), name='login-callback' ),
    path('logout/', LogoutView.as_view(), name='logout'),

    # api view
    path('reset/', LoginAPIView.as_view(), name='reset'),
    path('get-profile/', GetMemberProfileAPIView.as_view(), name='get-profile'),
    path('get-alarms-not-checked/', GetMemberAlarmsNotChckedAPIView.as_view(), name='get-alarms-not-checked'),
]