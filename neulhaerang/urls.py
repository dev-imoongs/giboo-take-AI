from django.urls import path

from neulhaerang.views import NeulhaerangDetailView, NeulhaerangListView, NeulhaerangAPIView, TestView, \
    NeulhaerangDetailReplyAPIView, NeulhaerangDetailReplyWriteAPIView, NeulhaerangDetailReplyLikeAPIView, \
    NeulhaerangDetailReplyDeleteAPIview, NeulhaerangDetailLikeAPIView, NeulhaerangDetailParticipateAPIView, \
    NeulhaerangDetailRealtimeFundAmountAPIView, SuccessPayment

app_name = 'neulhaerang'

urlpatterns = [
    path('list/', NeulhaerangListView.as_view(), name='list'),
    path('detail/<int:neulhaerang_id>/', NeulhaerangDetailView.as_view(), name='detail'),
    path('test/', TestView.as_view(), name ='test'),



    # api view
    path('list-api-view/', NeulhaerangAPIView.as_view(), name='list-api-view'),
    path('detail-reply-view/', NeulhaerangDetailReplyAPIView.as_view(), name='detail-reply-view'),
    path('detail-write-view/', NeulhaerangDetailReplyWriteAPIView.as_view(), name='detail-write-view'),
    path('detail-reply-like/', NeulhaerangDetailReplyLikeAPIView.as_view(), name='detail-reply-like'),
    path('detail-reply-delete/', NeulhaerangDetailReplyDeleteAPIview.as_view(), name='detail-reply-delete'),
    path('detail-neulhaerang-like/', NeulhaerangDetailLikeAPIView.as_view(), name='detail-neulhaerang-like'),
    path('detail-neulhaerang-participate/', NeulhaerangDetailParticipateAPIView.as_view(), name='detail-neulhaerang-participate'),
    path('detail-realtime-fundamount/', NeulhaerangDetailRealtimeFundAmountAPIView.as_view(), name='detail-realtime-fundamount'),
    path('detail-success-payment/', SuccessPayment.as_view(),name='detail-success-payment')
]