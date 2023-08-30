from django.urls import path

from neulhajang.views import NeulhajangListView, NeulhajangListAPIView, NeulhajangDetailView, \
    AuthenticationFeedListAPIView, NeulhajangLikeAPIView, NeulhajangActionFeedListAPIView, ActionFeedLikeAPIView, \
    NeulhajangNewsAPIView, AuthenticationFeedApplyAPIView

app_name = 'neulhajang'

urlpatterns = [
    path('list/', NeulhajangListView.as_view(), name='list'),
    path('detail/<int:neulhajang_id>/', NeulhajangDetailView.as_view(), name='detail'),

    # apiview
    path('neulhajang-list-api-view/', NeulhajangListAPIView.as_view(), name='neulhajang-list-api-view'),
    path('neulhajang-authentic-list/', AuthenticationFeedListAPIView.as_view(), name='neulhajang-authentic-list'),
    path('neulhajang-authentic-apply/', AuthenticationFeedApplyAPIView.as_view(), name='neulhajang-authentic-apply'),
    path('neulhajang-like/', NeulhajangLikeAPIView.as_view(), name='neulhajang-like'),
    path('neulhajang-action-feed-list/', NeulhajangActionFeedListAPIView.as_view(), name='neulhajang-action-feed-list'),
    path('neulhajang-action-feed-like/', ActionFeedLikeAPIView.as_view(), name='neulhajang-action-feed-like'),
    path('neulhajang-news/', NeulhajangNewsAPIView.as_view(), name='neulhajang-news')
]