from django.urls import path

from mypage.views import MypageBadgeView, MypageByeoljjiView, MypageDonateView, MypageSignOutView, \
    MypageServiceSettingView, MypageProfileView, MypagePostListView, MypageOthersLinkView, MypageMainView, \
    MypageReplyView, MemberChangeDonationStatusAPIView, TimeReplyTimeView, DonationListAPIView, \
    NeulhaerangListAPIView, NewMypagePostListView

app_name = 'mypage'

urlpatterns = [
    path('badge/',MypageBadgeView.as_view(),name = 'badge'),
    path('Byeoljji/',MypageByeoljjiView.as_view(),name = 'byeoljji'),
    path('donate/',MypageDonateView.as_view(),name = 'donate'),
    path('main/',MypageMainView.as_view(),name = 'main'),
    path('others-link/',MypageOthersLinkView.as_view(),name = 'otherslink'),
    path('post-list/',MypagePostListView.as_view(),name ='post-list'),
    path('profile/',MypageProfileView.as_view(),name = 'profile'),
    path('service-setting/',MypageServiceSettingView.as_view(),name = 'service-setting'),
    path('sign-out/',MypageSignOutView.as_view(),name = 'sign-out'),
    path('reply/', MypageReplyView.as_view(),name = 'reply'),
    path('save_data/', MypageProfileView.save_data, name='save_data'),
    path('donation_list/', DonationListAPIView.as_view(), name='donation_list'),
    path('member_neulhaerang_list/', NeulhaerangListAPIView.as_view(), name='member_neulhaerang_list'),

    # new post
    path('new-post-list/', NewMypagePostListView.as_view(), name='new-post-list'),

    # APIView 연결하는곳
    path('change-member-donation-status/',MemberChangeDonationStatusAPIView.as_view(),name= 'change-member-donation-status')
]