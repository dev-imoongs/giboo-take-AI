from django.urls import path

from neulhaerang.views import NeulhaerangDetailView, NeulhaerangListView, NeulhaerangAPIView, TestView, \
    NeulhaerangDetailReplyAPIView, NeulhaerangDetailReplyWriteAPIView, NeulhaerangDetailReplyLikeAPIView

app_name = 'neulhaerang'

urlpatterns = [
    path('list/', NeulhaerangListView.as_view(), name='list'),
    path('detail/<int:neulhaerang_id>', NeulhaerangDetailView.as_view(), name='detail'),
    path('test/', TestView.as_view(), name ='test'),



    # api view
    path('list-api-view/', NeulhaerangAPIView.as_view(), name='list-api-view'),
    path('detail-reply-view/', NeulhaerangDetailReplyAPIView.as_view(), name='detail-reply-view'),
    path('detail-write-view/', NeulhaerangDetailReplyWriteAPIView.as_view(), name='detail-write-view'),
    path('detail-reply-like/', NeulhaerangDetailReplyLikeAPIView.as_view(), name='detail-reply-like')
]