from django.urls import path

from neulhaerang.views import NeulhaerangDetailView, NeulhaerangListView, NeulhaerangAPIView, TestView

app_name = 'neulhaerang'

urlpatterns = [
    path('list/', NeulhaerangListView.as_view(), name='list'),
    path('detail/<int:neulhaerang_id>', NeulhaerangDetailView.as_view(), name='detail'),
    path('test/', TestView.as_view(), name ='test'),



    # api view
    path('list-api-view/', NeulhaerangAPIView.as_view(), name='list-api-view'),
    # path('list/<int:category_id>', NeulhaerangAPIView.as_view(), name='category-api-view'),
]