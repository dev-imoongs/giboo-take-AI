from django.urls import path

from mypage.views import MypageBadgeView, MypageByeoljjiView, MypageDonateView, MypageSignOutView, \
    MypageServiceSettingView, MypageProfileView, MypagePostListView, MypageOthersLinkView, MypageMainView, \
    MypageReplyView, MemberChangeDonationStatusAPIView, TimeReplyTimeView, DonationListAPIView, \
    MypageGetAthenticationFeedsByPagedAPIView, MypageDeleteAthenticationFeedAPIView, MypageGetRepliesByPagedAPIView, \
    MypageDeleteReplyAPIView, MypageGetByeoljjisByPagedAPIView, MypageGetBadgeInfoAPIView
from mypage.views2 import NewMypagePostListView, NewMypageNeulhajangPostListAPIView, NewMypageNeulhaerangPostListAPIView

app_name = 'mypage'

urlpatterns = [
    path('badge/',MypageBadgeView.as_view(),name = 'badge'),
    path('Byeoljji/',MypageByeoljjiView.as_view(),name = 'byeoljji'),
    path('donate/',MypageDonateView.as_view(),name = 'donate'),
    path('main/',MypageMainView.as_view(),name = 'main'),
    path('others-link/',MypageOthersLinkView.as_view(),name = 'otherslink'),
    path('post-list/',MypagePostListView.as_view(),name = 'post-list'),
    path('profile/',MypageProfileView.as_view(),name = 'profile'),
    path('service-setting/',MypageServiceSettingView.as_view(),name = 'service-setting'),
    path('sign-out/',MypageSignOutView.as_view(),name = 'sign-out'),
    path('reply/', MypageReplyView.as_view(),name = 'reply'),
    path('save_data/', MypageProfileView.save_data, name='save_data'),
    path('donation_list/', DonationListAPIView.as_view(), name='donation_list'),
    path('get-feeds/', MypageGetAthenticationFeedsByPagedAPIView.as_view(), name='get-feeds'),
    path('delete-feed/', MypageDeleteAthenticationFeedAPIView.as_view(), name='delete-feed'),

    path('get-replies/', MypageGetRepliesByPagedAPIView.as_view(), name='get-replies'),

    path('delete-reply/', MypageDeleteReplyAPIView.as_view(), name='delete-reply'),

    path('get-byeoljjis/', MypageGetByeoljjisByPagedAPIView.as_view(), name='get-byeoljjis'),
    path('get-badge-info/', MypageGetBadgeInfoAPIView.as_view(), name='get-badge-info'),

    # new post
    path('new-post-list/', NewMypagePostListView.as_view(), name='new-post-list'),
    path('new-post-neulhaerang-list-api/', NewMypageNeulhaerangPostListAPIView.as_view(), name='new-post-neulhaerang-list-api'),
    path('new-post-neulhajang-list-api/', NewMypageNeulhajangPostListAPIView.as_view(), name='new-post-neulhajang-list-api'),

    # APIView 연결하는곳
    path('change-member-donation-status/',MemberChangeDonationStatusAPIView.as_view(),name= 'change-member-donation-status')
]