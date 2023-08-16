from django.urls import path

from admin.views import AdminInqueryView

app_name = 'admin'

urlpatterns = [
    path('inquery/list/',AdminInqueryView.as_view(),name = 'inquery/list')
]