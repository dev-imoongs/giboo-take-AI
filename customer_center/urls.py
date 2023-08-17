from django.urls import path

from customer_center.views import AlarmView, CustomerCenterListView, InqueryWriteView

app_name = 'customer_center'

urlpatterns = [
    path('alarm/',AlarmView.as_view(),name="alarm"),
    path('list/',CustomerCenterListView.as_view(),name = "list"),
    path('inquery/write/',InqueryWriteView.as_view(),name = "inquery-write"),
]