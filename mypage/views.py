from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member
from neulhaerang.models import Neulhaerang


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

    def get(self, request):
        member = Member.objects.get(id=1)
        neulhaerang = Neulhaerang.objects.get(id=1)
        member.total_donation_fund = '{:,}'.format(member.total_donation_fund)
        member.total_donation_count = '{:,}'.format(member.total_donation_count)
        members = Member.objects.all()


        temp = Neulhaerang.objects.filter(member_id=1)[0:2]
        # print(abcd[i]['neulh'])
       # temp.append(abcd.neulhaerang_title)

        neulhaerang_count = Neulhaerang.objects.filter(member_id=1).count()


        context = {
                   # 회원 정보
                   'www_neulhaerang_title': temp,
                   'member_nickname': member.member_nickname,
                   'donation_level': member.donation_level,
                   'donation_status': member.donation_status,
                   'total_donation_fund': member.total_donation_fund,
                   'total_donation_count': member.total_donation_count,

                   # 내가 참여한 늘해랑 게시글

                   'volunteer_duration_start_date': neulhaerang.volunteer_duration_start_date,
                   'member_neulhaerang_count': neulhaerang_count,
                   # 댓글 총 갯수 여기부터 하면됌 댓글, 리뷰 떄려넣어놨음
                   # 'member_reply_count':


                   }
        return render(request, 'mypage/mypage-main.html', context)





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

class MypageReplyView(View):
    def get(self, request):
        return render(request, 'mypage/mypage-reply.html')

class MemberChangeDonationStatusAPIView(APIView):
    def get(self, request):
        member = Member.objects.get(id=1)
        if member.donation_status == "공개":
            member.donation_status = "비공개"
        else:
            member.donation_status = "공개"

        member.save()
        return Response(True)
