from django.urls import path

from neulhajang.views import NeulhajangListView

app_name = 'neulhajang'

urlpatterns = [
    path('list/', NeulhajangListView.as_view(),name ='list')
]