from django.urls import path

from customer_center.views import CustomerCenterListView, InqueryWriteView, AlarmView, GetAlarmsByPagedAPIView

app_name = 'customer_center'

urlpatterns = [
    path('alarm/',AlarmView.as_view(),name="alarm"),
    path('list/',CustomerCenterListView.as_view(),name = "list"),
    path('inquery/write/',InqueryWriteView.as_view(),name = "inquery-write"),

    path('get-alarms-by-paged/',GetAlarmsByPagedAPIView.as_view())
]