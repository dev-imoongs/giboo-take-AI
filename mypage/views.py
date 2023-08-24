from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DeleteView
from rest_framework.response import Response
from rest_framework.views import APIView


import neulhaerang_review
from member.models import Member
from neulhaerang.models import Neulhaerang, NeulhaerangReply, MemberByeoljji, Byeoljji
from neulhaerang_review.models import NeulhaerangReviewReply, NeulhaerangReview
from neulhajang.models import Neulhajang
from static_app.models import Badge, MemberBadge


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




    def get(self, request):
        member = Member.objects.get(id=1)

        profile_badge = MemberBadge.objects.filter(member_id=1)[0:1].get().badge.badge_image
        context = {
            #'www_neulhaerang_title': temp,
            'member_nickname': member.member_nickname,
            'donation_level': member.donation_level,
            'member_profile_image': member.profile_image,
            'member_profile_badge': profile_badge,
            'donation_status': member.donation_status,
            'total_donation_fund': member.total_donation_fund,
            'total_donation_count': member.total_donation_count,
        }
        return render(request, 'mypage/mypage-donate.html', context)


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

        profile_badge = MemberBadge.objects.filter(member_id=1)[0:1].get().badge.badge_image

        temp = Neulhaerang.objects.filter(member_id=1)[0:2]
        # temp = Neulhaerang.objects.filter(member__member_email = request.session['member_email'])[0:2]
        neulhajang_temp = Neulhajang.objects.filter(member_id=1)[0:2]
        reply_temp = NeulhaerangReviewReply.objects.filter(member_id=1)[0:2]
        badge_temp = MemberBadge.objects.filter(member_id=1)[0:5]
        byeoljji_temp = MemberByeoljji.objects.filter(member_id=1)[0:4]
        # print(abcd[i]['neulh'])
        # temp.append(abcd.neulhaerang_title)

        neulhaerang_count = Neulhaerang.objects.filter(member_id=1).count()
        neulhajang_count = Neulhajang.objects.filter(member_id=1).count()
        reply_neulhaerang = NeulhaerangReply.objects.filter(member_id=1).count()
        reply_neulhaerang_review = NeulhaerangReviewReply.objects.filter(member_id=1).count()
        byeoljji_count = MemberByeoljji.objects.filter(member_id=1).count()
        badge_count = MemberBadge.objects.filter(member_id=1).count()

        total_reply = (reply_neulhaerang + reply_neulhaerang_review)


        context = {
                   # 회원 정보
                   'www_neulhaerang': temp,
                   'www_neulhajang': neulhajang_temp,
                   'member_nickname': member.member_nickname,
                   'donation_level': member.donation_level,
                   'member_profile_image': member.profile_image,
                   'member_profile_badge': profile_badge,
                   'donation_status': member.donation_status,
                   'total_donation_fund': member.total_donation_fund,
                   'total_donation_count': member.total_donation_count,

                   # 내가 참여한 늘해랑 게시글

                   'volunteer_duration_start_date': neulhaerang.volunteer_duration_start_date,
                   'member_neulhaerang_count': neulhaerang_count,
                   'member_neulhajang_count': neulhajang_count,
                   # 'member_neulhaerang_img': neulhaerang.thumbnail_image,
                   # 댓글 총 갯수 여기부터 하면됌 댓글, 리뷰 때려넣어놨음
                   'member_reply_count': total_reply,
                   # 'member_reply_review_content': reply_temp,
                   'www_reply_content': reply_temp,
                   # 'reply_title': review_title,

                   # 뱃지
                   'www_badge_content': badge_temp,
                   'www_byeoljji_content': byeoljji_temp,
                   'byeoljji_count': byeoljji_count,
                   'badge_count': badge_count,

                   }
        return render(request, 'mypage/mypage-main.html', context)



class MypageOthersLinkView(View):
    def get(self,request):
        return render(request, 'mypage/mypage-otherslink.html')


class MypagePostListView(View):
    def get(self,request):
        return render(request, 'mypage/mypage-post-list.html')


class MypageProfileView(View):

    def get(self, request):
        member = Member.objects.get(member_email=request.session['member_email'])

        context = {
            'profile_image': member.profile_image,
            'member_nickname': member.member_nickname,
            'member_email': member.member_email,
            'member_age': member.member_age,
            'member_gender':member.member_gender,


        }

        return render(request, 'mypage/mypage-profile.html', context)

    def save_data(request):

        if request.method == 'POST':
            member_email = request.session.get('member_email')
            print(request.POST)
            if member_email:
                # 세션에서 이메일을 사용하여 멤버를 가져옵니다. 이메일을 기반으로 멤버를 식별해야 합니다.
                member = get_object_or_404(Member, member_email=member_email)
                member_nickname = request.POST.get('member_nickname', '찐빵로봇')
                member_gender = request.POST.get('genderChk', 'notselect')

                # 멤버 필드 값을 업데이트하고 저장합니다.
                member.member_nickname = member_nickname
                print(member_nickname)

                member.member_gender = member_gender
                print(member_gender)
                member.save()

                return redirect('success_page')

        return JsonResponse({'error': '잘못된 요청입니다.'})

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
