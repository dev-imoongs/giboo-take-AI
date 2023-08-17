from django.shortcuts import render
from django.views import View


# Create your views here.



class MypageBadgeView(View):
    def get(self,request):
        return render(request, 'mypage/mypage-badge.html')


class MypageByeoljjiView(View):
    def get(self,request):
        return render(request, 'mypage/mypage-byeoljji.html')


class MypageDonateView(View):
    def get(self,request):
        return render(request, 'mypage/mypage-donate.html')


class MypageMainView(View):
    def get(self,request):
        return render(request, 'mypage/mypage-main.html')


class MypageOthersLinkView(View):
    def get(self,request):
        return render(request, 'mypage/mypage-otherslink.html')


class MypagePostListView(View):
    def get(self,request):
        return render(request, 'mypage/mypage-post-list.html')


class MypageProfileView(View):
    def get(self,request):
        return render(request, 'mypage/mypage-profile.html')


class MypageReplyView(View):
    def get(self,request):
        return render(request, 'mypage/mypage-reply.html')


class MypageServiceSettingView(View):
    def get(self,request):
        return render(request, 'mypage/mypage-sevice-settings.html')


class MypageSignOutView(View):
    def get(self, request):
        return render(request, 'mypage/mypage-sign-out.html')



