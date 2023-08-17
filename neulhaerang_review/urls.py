from django.urls import path

from neulhaerang_review.views import NeulhaerangReviewListView, NeulhaerangReviewDetailView

app_name = 'neulhaerang_review'

urlpatterns = [
path('review/list/', NeulhaerangReviewListView.as_view(),name='review-list'),
    path('review/detail/', NeulhaerangReviewDetailView.as_view(),name='review-detail'),
]