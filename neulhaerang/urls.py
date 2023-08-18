from django.urls import path

from neulhaerang.views import NeulhaerangDetailView, NeulhaerangListView, NeulhaerangAPIView

app_name = 'neulhaerang'

urlpatterns = [
    path('list/', NeulhaerangListView.as_view(), name='list'),
    path('detail/', NeulhaerangDetailView.as_view(), name='detail'),




    # api view
    path('list-api-view/', NeulhaerangAPIView.as_view(), name='list-api-view')
]