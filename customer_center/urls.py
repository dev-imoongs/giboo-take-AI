from django.urls import path

from customer_center.views import AlarmView, CustomerCenterListView, InqueryWriteView

app_name = 'customer_center'

urlpatterns = [
    path('alarm/',AlarmView.as_view()),
    path('list/',CustomerCenterListView.as_view()),
    path('inquery/write/',InqueryWriteView.as_view()),
]