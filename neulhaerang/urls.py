from django.urls import path

from neulhaerang.views import NeulhaerangDetailView, NeulhaerangListView


app_name = 'neulhaerang'

urlpatterns = [
    path('list/', NeulhaerangListView.as_view(), name='list'),
    path('detail/', NeulhaerangDetailView.as_view(), name='detail'),
]