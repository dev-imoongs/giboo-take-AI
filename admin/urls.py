from django.urls import path

from admin.views import AdminInqueryListView, AdminMemberListView, AdminNeulhaerangListView, \
    AdminNeulhaerangDetailView, AdminNeulhajangListView, AdminNeulhajangDetailView, AdminNoticeWriteView, \
    AdminNoticeListView, AdminReviewListView, AdminMainView, \
    AdminGetMembersByPagedAPIView, AdminChangeMemberStatusAPIView, \
    AdminDeleteNeulhaerangAPIView, AdminGetNeulhajangsByPagedAPIView, AdminDeleteNeulhajangAPIView, \
    AdminGetNeulhaerangsByPagedAPIView, AdminGetReviewsByPagedAPIView, AdminDeleteReviewAPIView, \
    AdminGetNoticesByPagedAPIView, AdminDeleteNoticeAPIView, AdminNoticeDetailView, AdminGetInquerysByPagedAPIView, \
    AdminDeleteInquerysAPIView, AdminInqueryDetailView

app_name = 'admin'




urlpatterns = [
    path('main/', AdminMainView.as_view(), name='main'),
    path('inquery/list/', AdminInqueryListView.as_view(), name='inquery/list'),
    path('inquery/detail/', AdminInqueryDetailView.as_view(), name='inquery/detail'),
    path('member/list/', AdminMemberListView.as_view(), name='member/list'),
    path('neulhaerang/list/', AdminNeulhaerangListView.as_view(), name='neulhaerang/list'),
    path('neulhaerang/detail/', AdminNeulhaerangDetailView.as_view(), name='neulhaerang/detail'),
    path('neulhajang/list/', AdminNeulhajangListView.as_view(), name='neulhajang/list'),
    path('neulhajang/detail/', AdminNeulhajangDetailView.as_view(), name='neulhajang/detail'),
    path('notice/list/', AdminNoticeListView.as_view(), name='notice/list'),
    path('notice/detail/', AdminNoticeDetailView.as_view(), name='notice/detail'),
    path('notice/write/', AdminNoticeWriteView.as_view(), name='notice/write'),
    path('review/list/', AdminReviewListView.as_view(), name='review/list'),




    #rest api view
    path('get-members-by-paged/',AdminGetMembersByPagedAPIView.as_view(),name ='get-members-by-paged'),
    path('change-member-status/',AdminChangeMemberStatusAPIView.as_view()),
    path('get-neulhaerangs-by-paged/', AdminGetNeulhaerangsByPagedAPIView.as_view()),
    path('delete-neulhaerangs/', AdminDeleteNeulhaerangAPIView.as_view()),
    path('get-neulhajangs-by-paged/', AdminGetNeulhajangsByPagedAPIView.as_view()),
    path('delete-neulhajangs/', AdminDeleteNeulhajangAPIView.as_view()),
    path('get-reviews-by-paged/', AdminGetReviewsByPagedAPIView.as_view()),
    path('delete-reviews/', AdminDeleteReviewAPIView.as_view()),

    path('get-notices-by-paged/', AdminGetNoticesByPagedAPIView.as_view()),
    path('delete-notices/', AdminDeleteNoticeAPIView.as_view()),
    path('get-inquerys-by-paged/', AdminGetInquerysByPagedAPIView.as_view()),
    path('delete-inquerys/', AdminDeleteInquerysAPIView.as_view()),

]
