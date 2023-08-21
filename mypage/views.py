from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DeleteView
from rest_framework.response import Response
from rest_framework.views import APIView


import neulhaerang_review
from member.models import Member
from neulhaerang.models import Neulhaerang, NeulhaerangReply
from neulhaerang_review.models import NeulhaerangReviewReply, NeulhaerangReview


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

# class MypageMainDeleteView(View):
#     def get(self, request, review_reply_id):
#         NeulhaerangReviewReply.objects.get(id=review_reply_id).delete(id=9)
#         return redirect('neulhaerang_review:review/list')




class MypageMainView(View):
    def get(self,request):
        return render(request, 'mypage/mypage-main.html')

    def get(self, request):
        member = Member.objects.get(id=1)
        neulhaerang = Neulhaerang.objects.get(id=1)
        member.total_donation_fund = '{:,}'.format(member.total_donation_fund)
        member.total_donation_count = '{:,}'.format(member.total_donation_count)
        # neulhaerang_review = NeulhaerangReview.objects.get(id=1)
        # review_title = neulhaerang_review_reply.neulhaerang_review.neulhaerang_review_title

        temp = Neulhaerang.objects.filter(member_id=1)[0:2]
        reply_temp = NeulhaerangReviewReply.objects.filter(member_id=1)[0:2]

        # print(abcd[i]['neulh'])
        # temp.append(abcd.neulhaerang_title)

        neulhaerang_count = Neulhaerang.objects.filter(member_id=1).count()
        reply_neulhaerang = NeulhaerangReply.objects.filter(member_id=1).count()
        reply_neulhaerang_review = NeulhaerangReviewReply.objects.filter(member_id=1).count()

        total_reply = (reply_neulhaerang + reply_neulhaerang_review)


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
                   'member_neulhaerang_img': neulhaerang.thumbnail_image,
                   # 댓글 총 갯수 여기부터 하면됌 댓글, 리뷰 때려넣어놨음
                   'member_reply_count': total_reply,
                   # 'member_reply_review_content': reply_temp,
                   'www_reply_content': reply_temp,
                   # 'reply_title': review_title,



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

class TimeReplyTimeView(APIView):
    def get(self, request):
        return render(request, 'mypage/mypage-main.html')
