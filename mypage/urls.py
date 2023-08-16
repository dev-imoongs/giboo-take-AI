from django.urls import path

from mypage.views import MypageBadgeView, MypageByeoljjiView, MypageDonateView, MypageSignOutView, \
    MypageServiceSettingView, MypageProfileView, MypagePostListView, MypageOthersLinkView

app_name = 'mypage'

urlpatterns = [
    path('badge/',MypageBadgeView.as_view()),
    path('Byeoljji/',MypageByeoljjiView.as_view()),
    path('donate/',MypageDonateView.as_view()),
    path('main/',MypageBadgeView.as_view()),
    path('others-link/',MypageOthersLinkView.as_view()),
    path('post-list/',MypagePostListView.as_view()),
    path('profile/',MypageProfileView.as_view()),
    path('service-setting/',MypageServiceSettingView.as_view()),
    path('sign-out/',MypageSignOutView.as_view()),
]