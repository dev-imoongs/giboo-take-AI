from django.shortcuts import render
from django.views import View


# Create your views here.



class MypageBadgeView(View):
    def get(self,request):
        return render(request, 'mypage/mypage_badge.html')


class MypageByeoljjiView(View):
    def get(self,request):
        return render(request, 'mypage/mypage_byeoljji.html')


class MypageDonateView(View):
    def get(self,request):
        return render(request, 'mypage/mypage_donate.html')


class MypageMainView(View):
    def get(self,request):
        return render(request, 'mypage/mypage_main.html')


class MypageOthersLinkView(View):
    def get(self,request):
        return render(request, 'mypage/mypage_otherslink.html')


class MypagePostListView(View):
    def get(self,request):
        return render(request, 'mypage/mypage_post_list.html')


class MypageProfileView(View):
    def get(self,request):
        return render(request, 'mypage/mypage_profile.html')


class MypageReplyView(View):
    def get(self,request):
        return render(request, 'mypage/mypage_reply.html')


class MypageServiceSettingView(View):
    def get(self,request):
        return render(request, 'mypage/mypage_sevice_settings.html')


class MypageSignOutView(View):
    def get(self, request):
        return render(request, 'mypage/mypage_sign-out.html')



