from django.urls import path

from neulhaerang.views import NeulhaerangDetailView, NeulhaerangListView, NeulhaerangReviewListView, \
    NeulhaerangReviewDetailView

app_name = 'neulhaerang'

urlpatterns = {
    path('list/', NeulhaerangListView.as_view()),
    path('detail/', NeulhaerangDetailView.as_view()),
    path('review/list/', NeulhaerangReviewListView.as_view()),
    path('review/detail/', NeulhaerangReviewDetailView.as_view()),
}