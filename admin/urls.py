from django.urls import path

from admin.views import AdminInqueryListView, AdminInqueryWriteView, AdminMemberListView, AdminNeulhaerangListView, \
    AdminNeulhaerangDetailView, AdminNeulhajangListView, AdminNeulhajangDetailView, AdminNoticeWriteView, \
    AdminNoticeListView, AdminNoticeUpdateView, AdminReviewListView, AdminReviewDetailView, AdminMainView

app_name = 'admin'

urlpatterns = [
    path('main/',AdminMainView.as_view(),name = 'main'),
    path('inquery/list/',AdminInqueryListView.as_view(),name = 'inquery/list'),
    path('inquery/write/',AdminInqueryWriteView.as_view(),name = 'inquery/write'),
    path('member/list/',AdminMemberListView.as_view(),name = 'member/list'),
    path('neulhaerang/list/',AdminNeulhaerangListView.as_view(),name = 'neulhaerang/list'),
    path('neulhaerang/detail/',AdminNeulhaerangDetailView.as_view(),name = 'neulhaerang/detail'),
    path('neulhajang/list/',AdminNeulhajangListView.as_view(),name = 'neulhajang/list'),
    path('neulhajang/detail/',AdminNeulhajangDetailView.as_view(),name = 'neulhajang/detail'),
    path('notice/list/',AdminNoticeListView.as_view(),name = 'notice/list'),
    path('notice/write/',AdminNoticeWriteView.as_view(),name = 'notice/write'),
    path('notice/update/',AdminNoticeUpdateView.as_view(),name = 'notice/update'),
    path('review/list/',AdminReviewListView.as_view(),name = 'review/list'),
    path('review/detail/',AdminReviewDetailView.as_view(),name = 'review/detail'),
]