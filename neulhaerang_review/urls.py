from django.urls import path

from neulhaerang_review.views import NeulhaerangReviewListView, NeulhaerangReviewDetailView, \
    NeulhaerangReviewListAPIView

app_name = 'neulhaerang_review'

urlpatterns = [


    path('review/list/', NeulhaerangReviewListView.as_view(),name='review/list'),
    path('review/detail/<int:neulhaerang_review_id>', NeulhaerangReviewDetailView.as_view(),name='review/detail'),



#     api view
    path('review-list-api-view/', NeulhaerangReviewListAPIView.as_view(), name='review-list-api-view'),


]