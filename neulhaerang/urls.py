from django.urls import path

from neulhaerang.views import NeulhaerangDetailView, NeulhaerangListView, NeulhaerangReviewListView, \
    NeulhaerangReviewDetailView

app_name = 'neulhaerang'

urlpatterns = [
    path('list/', NeulhaerangListView.as_view(), name='list'),
    path('detail/', NeulhaerangDetailView.as_view(), name='detail'),
    path('review/list/', NeulhaerangReviewListView.as_view(), name='review'),
    path('review/detail/', NeulhaerangReviewDetailView.as_view(), name='review/detail'),
]