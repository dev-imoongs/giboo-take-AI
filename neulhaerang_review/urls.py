from django.urls import path

from neulhaerang_review.views import NeulhaerangReviewListView, NeulhaerangReviewDetailView, \
    NeulhaerangReviewListAPIView, NeulhaerangReviewDetailReplyAPIView, NeulhaerangReviewDetailReplyWriteAPIView, \
    NeulhaerangReviewDetailReplyDeleteAPIview, NeulhaerangReviewDetailReplyLikeAPIView, \
    NeulhaerangReviewDetailLikeAPIView

app_name = 'neulhaerang_review'

urlpatterns = [



    path('review/list/', NeulhaerangReviewListView.as_view(),name='review/list'),
    path('review/detail/<int:neulhaerang_review_id>/', NeulhaerangReviewDetailView.as_view(),name='review/detail'),



#     api view
    path('review-list-api-view/', NeulhaerangReviewListAPIView.as_view(), name='review-list-api-view'),
    path('review-detail-reply/', NeulhaerangReviewDetailReplyAPIView.as_view(), name='review-detail-reply'),
    path('review-detail-reply-write/', NeulhaerangReviewDetailReplyWriteAPIView.as_view(), name='review-detail-reply-write'),
    path('review-detail-reply-delete/', NeulhaerangReviewDetailReplyDeleteAPIview.as_view(), name='review-detail-reply-delete'),
    path('review-detail-reply-like/', NeulhaerangReviewDetailReplyLikeAPIView.as_view(), name='review-detail-reply-like'),
    path('review-detail-like/', NeulhaerangReviewDetailLikeAPIView.as_view(), name='review-detail-like')
]