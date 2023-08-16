from django.urls import path

from notice.views import NoticeListView, NoticeDetailView

app_name = 'notice'

urlpatterns = [
    path('list/',NoticeListView.as_view()),
    path('detail/',NoticeDetailView.as_view()),
]