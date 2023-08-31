import json
from datetime import datetime
import random

import requests
from django.db.models import Value, Count, F, Sum
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DeleteView
from rest_framework.response import Response
from rest_framework.views import APIView


import neulhaerang_review
from customer_center.models import Alarm
from member.models import Member
from neulhaerang.models import Neulhaerang, NeulhaerangReply, MemberByeoljji, Byeoljji, NeulhaerangDonation, \
    BusinessPlan, NeulhaerangInnerTitle, NeulhaerangInnerContent, NeulhaerangTag, NeulhaerangInnerPhotos
from neulhaerang_review.models import NeulhaerangReviewReply, NeulhaerangReview, FundUsageHistory, ReviewInnerTitle, \
    ReviewInnerContent, NeulhaerangReviewTag, ReviewInnerPhotos
from neulhajang.models import Neulhajang, NeulhajangAuthenticationFeed, NeulhajangMission, NeulhajangInnerTitle, \
    NeulhajangInnerContent, NeulhajangInnerPhoto
from static_app.models import Badge, MemberBadge, Category
from workspace.pagenation import Pagenation
from workspace.serializers import PagenatorSerializer, NeulhaerangSerializer, NeulhaerangDonationSerializer


# Create your views here.



class MypageBadgeView(View):
    def get(self, request):
        member = Member.objects.get(member_email=request.session.get("member_email"))
        profile_badge = MemberBadge.objects.filter(member=member)
        if profile_badge:
            profile_badge = profile_badge.values('member','badge').annotate(badge_total=Count('id')).annotate(badge_name=F("badge__badge_name")).annotate(badge_image=F("badge__badge_image")).order_by('-badge_total').first().get("badge_image")
        else:
            profile_badge = ""
        badge_temp = MemberBadge.objects.filter(member=member).values('member','badge').annotate(badge_total=Count('id')).annotate(badge_name=F("badge__badge_name")).annotate(badge_image=F("badge__badge_image")).annotate(badge_id = F("badge"))
        nobadge_temp = Badge.objects.exclude(memberbadge__member = member).distinct()
        badge_count = MemberBadge.objects.filter(member=member).values('member','badge').annotate(badge_total=Count('id')).count()

        context = {
            'profile_image': member.profile_image,
            'member_nickname': member.member_nickname,
            'member_email': member.member_email,
            'member_age': member.member_age,
            'member_gender':member.member_gender,
            'member': member,
            'member_profile_badge': profile_badge,
            'donation_level': member.donation_level,
            'www_badge_list': badge_temp,
            'www_nobadge_list': nobadge_temp,
            'badge_count': badge_count,
            'modal_badge_name': Badge.badge_name,
        }

        return render(request, 'mypage/mypage-badge.html', context)


class MypageByeoljjiView(View):
    def get(self,request):

        member_email = request.session.get('member_email')

        if member_email:
            try:
                member = Member.objects.get(member_email=member_email)

                profile_badge = MemberBadge.objects.filter(member=member)
                if profile_badge:
                    profile_badge = profile_badge.values('member', 'badge').annotate(badge_total=Count('id')).annotate(
                        badge_name=F("badge__badge_name")).annotate(badge_image=F("badge__badge_image")).order_by(
                        '-badge_total').first().get("badge_image")

                else:
                    profile_badge = ''
                byeoljji_count = MemberByeoljji.objects.filter(member=member).count()

                context = {
                    'member_nickname': member.member_nickname,
                    'donation_level': member.donation_level,
                    'member_profile_image': member.profile_image,
                    'member_profile_badge': profile_badge,
                    'donation_status': member.donation_status,
                    'total_donation_fund': member.total_donation_fund,
                    'total_donation_count': member.total_donation_count,
                    'member': member,
                    'byeoljji_count':byeoljji_count,

                }

                return render(request, 'mypage/mypage-byeoljji.html', context)

            except Member.DoesNotExist:
                # 멤버가 존재하지 않는 경우 처리
                pass

        # 멤버 이메일이 세션에 존재하지 않거나 오류 발생 시
        return HttpResponse('잘못된 요청입니다.')


class MypageDonateView(View):

    def get(self, request):
        # 세션에서 멤버 이메일을 가져옵니다.
        member_email = request.session.get('member_email')

        if member_email:
            try:
                member = Member.objects.get(member_email=member_email)

                profile_badge = MemberBadge.objects.filter(member=member)
                if profile_badge:
                    profile_badge = profile_badge.values('member','badge').annotate(badge_total=Count('id')).annotate(badge_name=F("badge__badge_name")).annotate(badge_image=F("badge__badge_image")).order_by('-badge_total').first().get("badge_image")

                else :
                    profile_badge=''
                print(profile_badge)


                donation_temp = NeulhaerangDonation.objects.filter(member=member)[0:20]
                context = {
                    'www_donation_list': donation_temp,
                    'member_nickname': member.member_nickname,
                    'donation_level': member.donation_level,
                    'member_profile_image': member.profile_image,
                    'member_profile_badge': profile_badge,
                    'donation_status': member.donation_status,
                    'total_donation_fund': member.total_donation_fund,
                    'total_donation_count': member.total_donation_count,
                    'member':member,

                }

                return render(request, 'mypage/mypage-donate.html', context)

            except Member.DoesNotExist:
                # 멤버가 존재하지 않는 경우 처리
                pass

        # 멤버 이메일이 세션에 존재하지 않거나 오류 발생 시
        return HttpResponse('잘못된 요청입니다.')





    # def get(self, request):
    #     member = Member.objects.get(member_email=request.session['member_email'])
    #
    #     profile_badge = MemberBadge.objects.filter(member_id=1)[0:1].get().badge.badge_image
    #     print(request.session.get("member_email"))
    #     context = {
    #         #'www_neulhaerang_title': temp,
    #         'member_nickname': member.member_nickname,
    #         'donation_level': member.donation_level,
    #         'member_profile_image': member.profile_image,
    #         'member_profile_badge':  profile_badge,
    #         'donation_status': member.donation_status,
    #         'total_donation_fund': member.total_donation_fund,
    #         'total_donation_count': member.total_donation_count,
    #     }
    #     return render(request, 'mypage/mypage-donate.html', context)


# class MypageMainDeleteView(View):
#     def get(self, request, review_reply_id):
#         NeulhaerangReviewReply.objects.get(id=review_reply_id).delete(id=9)
#         return redirect('neulhaerang_review:review/list')




class MypageMainView(View):
    def get(self,request):
        return render(request, 'mypage/mypage-main.html')

    # def get(self, request):
    #     member = Member.objects.get(id=1)
    #     neulhaerang = Neulhaerang.objects.get(id=1)
    #
    #     member.total_donation_fund = '{:,}'.format(member.total_donation_fund)
    #     member.total_donation_count = '{:,}'.format(member.total_donation_count)
    #     # neulhaerang_review = NeulhaerangReview.objects.get(id=1)
    #     # review_title = neulhaerang_review_reply.neulhaerang_review.neulhaerang_review_title
    #
    #     profile_badge = MemberBadge.objects.filter(member_id=1)[0:1].get().badge.badge_image
    #
    #     temp = Neulhaerang.objects.filter(member_id=1)[0:2]
    #     # temp = Neulhaerang.objects.filter(member__member_email = request.session['member_email'])[0:2]
    #     neulhajang_temp = Neulhajang.objects.filter(member_id=1)[0:2]
    #     reply_temp = NeulhaerangReviewReply.objects.filter(member_id=1)[0:2]
    #     badge_temp = MemberBadge.objects.filter(member_id=1)[0:5]
    #     byeoljji_temp = MemberByeoljji.objects.filter(member_id=1)[0:4]
    #     # print(abcd[i]['neulh'])
    #     # temp.append(abcd.neulhaerang_title)
    #
    #     neulhaerang_count = Neulhaerang.objects.filter(member_id=1).count()
    #     neulhajang_count = Neulhajang.objects.filter(member_id=1).count()
    #     reply_neulhaerang = NeulhaerangReply.objects.filter(member_id=1).count()
    #     reply_neulhaerang_review = NeulhaerangReviewReply.objects.filter(member_id=1).count()
    #     byeoljji_count = MemberByeoljji.objects.filter(member_id=1).count()
    #     badge_count = MemberBadge.objects.filter(member_id=1).count()
    #
    #     total_reply = (reply_neulhaerang + reply_neulhaerang_review)
    #
    #
    #     context = {
    #                # 회원 정보
    #                'www_neulhaerang': temp,
    #                'www_neulhajang': neulhajang_temp,
    #                'member_nickname': member.member_nickname,
    #                'donation_level': member.donation_level,
    #                'member_profile_image': member.profile_image,
    #                'member_profile_badge': profile_badge,
    #                'donation_status': member.donation_status,
    #                'total_donation_fund': member.total_donation_fund,
    #                'total_donation_count': member.total_donation_count,
    #
    #                # 내가 참여한 늘해랑 게시글
    #
    #                'volunteer_duration_start_date': neulhaerang.volunteer_duration_start_date,
    #                'member_neulhaerang_count': neulhaerang_count,
    #                'member_neulhajang_count': neulhajang_count,
    #                # 'member_neulhaerang_img': neulhaerang.thumbnail_image,
    #                # 댓글 총 갯수 여기부터 하면됌 댓글, 리뷰 때려넣어놨음
    #                'member_reply_count': total_reply,
    #                # 'member_reply_review_content': reply_temp,
    #                'www_reply_content': reply_temp,
    #                # 'reply_title': review_title,
    #
    #                # 뱃지
    #                'www_badge_content': badge_temp,
    #                'www_byeoljji_content': byeoljji_temp,
    #                'byeoljji_count': byeoljji_count,
    #                'badge_count': badge_count,
    #
    #                }
    #     return render(request, 'mypage/mypage-main.html', context)


    def get(self, request):
        member_email = request.session.get('member_email')
        if member_email:
            member = get_object_or_404(Member, member_email=member_email)


            neulhaerang = Neulhaerang.objects.filter(member=member)

            member.total_donation_fund = '{:,}'.format(member.total_donation_fund)
            member.total_donation_count = '{:,}'.format(member.total_donation_count)

            profile_badge = MemberBadge.objects.filter(member=member)
            if profile_badge:
                profile_badge = profile_badge.values('member', 'badge').annotate(badge_total=Count('id')).annotate(
                    badge_name=F("badge__badge_name")).annotate(badge_image=F("badge__badge_image")).order_by(
                    '-badge_total').first().get("badge_image")
            else:
                profile_badge=''


            feeds = NeulhajangAuthenticationFeed.objects.filter(member=member)
            feeds_count = feeds.count()
            feeds = feeds[0:2]




            temp = Neulhaerang.objects.filter(member=member)[0:2]
            neulhajang_temp = Neulhajang.objects.filter(member=member)[0:2]
            reply_temp = NeulhaerangReviewReply.objects.filter(member=member)[0:2]
            byeoljji_temp = MemberByeoljji.objects.filter(member=member)[0:4]

            neulhaerang_count = Neulhaerang.objects.filter(member=member).count()
            neulhajang_count = Neulhajang.objects.filter(member=member).count()
            byeoljji_count = MemberByeoljji.objects.filter(member=member).count()

            badge_temp = MemberBadge.objects.filter(member=member).values('member', 'badge').annotate(
                badge_total=Count('id')).annotate(badge_name=F("badge__badge_name")).annotate(
                badge_image=F("badge__badge_image")).annotate(badge_id = F("badge"))
            nobadge_temp = Badge.objects.exclude(memberbadge__member=member).distinct()
            badge_count = MemberBadge.objects.filter(member=member).values('member', 'badge').annotate(
                badge_total=Count('id')).count()
            reply_neulhaerang = NeulhaerangReply.objects.filter(member=member,donation__isnull=True).annotate(type = Value("늘해랑")).annotate(like_count=Count("replylike"))
            reply_neulhaerang_review = NeulhaerangReviewReply.objects.filter(member=member).annotate(type=Value("후기")).annotate(like_count=Count("reviewreplylike"))

            total_reply = list(reply_neulhaerang) + list(reply_neulhaerang_review)
            total_reply_sorted = sorted(total_reply, key=lambda item: item.created_date)
            total_reply_sorted.reverse()

            print(total_reply_sorted)
            total_reply_count = (reply_neulhaerang.count() + reply_neulhaerang_review.count())
            print(total_reply_count)


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
                       'member':member,
                       'neulhaerang':neulhaerang,


                       # 내가 참여한 늘해랑 게시글

                       'volunteer_duration_start_date': Neulhaerang.volunteer_duration_start_date,
                       'member_neulhaerang_count': neulhaerang_count,
                       'member_neulhajang_count': neulhajang_count,
                       # 'member_neulhaerang_img': neulhaerang.thumbnail_image,
                       # 댓글 총 갯수 여기부터 하면됌 댓글, 리뷰 때려넣어놨음
                       'member_reply_count': total_reply,
                       # 'member_reply_review_content': reply_temp,
                       'www_reply_content': reply_temp,
                       # 'reply_title': review_title,

                       # 뱃지
                       'www_byeoljji_content': byeoljji_temp,
                       'byeoljji_count': byeoljji_count,


                        'www_badge_list': badge_temp[0:5],
                        'www_nobadge_list': nobadge_temp,
                        'badge_count': badge_count,



                        'feeds':feeds,
                        'feeds_count':feeds_count,
                        'total_reply_sorted':total_reply_sorted[:2],
                        "total_reply_count" : total_reply_count,

                       }
            return render(request, 'mypage/mypage-main.html', context)


class MypageOthersLinkView(View):
    def get(self,request):
        return render(request, 'mypage/mypage-otherslink.html')


class MypagePostListView(View):
    def get(self, request):
        member = Member.objects.get(member_email=request.session['member_email'])
        neulhaerang = Neulhaerang.objects.filter(member=member)
        member_neulhaerang_count =Neulhaerang.objects.filter(member=member).count()
        profile_badge = MemberBadge.objects.filter(member=member)
        if profile_badge:
            profile_badge = profile_badge.values('member','badge').annotate(badge_total=Count('id')).annotate(badge_name=F("badge__badge_name")).annotate(badge_image=F("badge__badge_image")).order_by('-badge_total').first().get("badge_image")
        else:
            profile_badge=''

        feeds = NeulhajangAuthenticationFeed.objects.filter(member=member)
        feeds_count = feeds.count()





        context = {
            'member_level': member.donation_level,
            'profile_image': member.profile_image,
            'member_nickname': member.member_nickname,
            'member_email': member.member_email,
            'member_age': member.member_age,
            'member_gender':member.member_gender,
            'member': member,
            'neulhaerang':neulhaerang,
            'member_nuelhaerang_count':member_neulhaerang_count,
            'member_profile_badge':profile_badge,
            'feeds_count':feeds_count,

        }
        return render(request, 'mypage/mypage-post-list.html',context)



class MypageProfileView(View):

    def get(self, request):
        member = Member.objects.get(member_email=request.session['member_email'])
        context = {
            'profile_image': member.profile_image,
            'member_nickname': member.member_nickname,
            'member_email': member.member_email,
            'member_age': member.member_age,
            'member_gender':member.member_gender,
            'member': member,

        }


        return render(request, 'mypage/mypage-profile.html', context)

    def save_data(request):

        if request.method == 'POST':
            member_email = request.session.get('member_email')
            if member_email:
                member = get_object_or_404(Member, member_email=member_email)
                member_nickname = request.POST.get('member_nickname', '닉네임을 지정해주세요')
                member_gender = request.POST.get('genderChk')
                profile_image = request.FILES.get('profile_image')



                files = request.FILES
                x_falg = request.POST.get("xFlag")
                kakao_falg = request.POST.get("kakaoFlag")
                print(kakao_falg)
                file = files.get("profile_image")
                if file:
                    member.profile_image = file
                    member.profile_image_choice = "user"
                elif x_falg == "true":
                    member.profile_image = ''
                    member.profile_image_choice = "user"
                elif kakao_falg =="true":
                    member.profile_image = request.session.get("kakao_image_url")
                    member.profile_image_choice = "kakao"
                member.member_nickname = member_nickname

                member.member_gender = member_gender
                member.save()

                return redirect('mypage:main')

        return JsonResponse({'error': '잘못된 요청입니다.'})




class MypageReplyView(View):
    def get(self,request):
        # 세션에서 멤버 이메일을 가져옵니다.
        member_email = request.session.get('member_email')

        if member_email:
            try:
                member = Member.objects.get(member_email=member_email)

                profile_badge = MemberBadge.objects.filter(member=member)
                if profile_badge:
                    profile_badge = profile_badge.values('member','badge').annotate(badge_total=Count('id')).annotate(badge_name=F("badge__badge_name")).annotate(badge_image=F("badge__badge_image")).order_by('-badge_total').first().get("badge_image")
                else:
                    profile_badge = ''

                request.session['profile_badge'] = profile_badge

                reply_neulhaerang = NeulhaerangReply.objects.filter(member=member, donation__isnull=True).annotate(
                    type=Value("늘해랑")).annotate(like_count=Count("replylike"))
                reply_neulhaerang_review = NeulhaerangReviewReply.objects.filter(member=member).annotate(
                    type=Value("후기")).annotate(like_count=Count("reviewreplylike"))

                total_reply = list(reply_neulhaerang) + list(reply_neulhaerang_review)
                total_reply_sorted = sorted(total_reply, key=lambda item: item.created_date)
                total_reply_sorted.reverse()

                print(total_reply_sorted)
                total_reply_count = (reply_neulhaerang.count() + reply_neulhaerang_review.count())
                print(total_reply_count)



                donation_temp = NeulhaerangDonation.objects.filter(member=member)[0:20]
                context = {
                    'www_donation_list': donation_temp,
                    'member_nickname': member.member_nickname,
                    'donation_level': member.donation_level,
                    'member_profile_image': member.profile_image,
                    'member_profile_badge': profile_badge,
                    'donation_status': member.donation_status,
                    'total_donation_fund': member.total_donation_fund,
                    'total_donation_count': member.total_donation_count,
                    'member': member,
                    'total_reply_count': total_reply_count,

                }

                return render(request, 'mypage/mypage-reply.html', context)

            except Member.DoesNotExist:
                # 멤버가 존재하지 않는 경우 처리
                pass

        # 멤버 이메일이 세션에 존재하지 않거나 오류 발생 시
        return HttpResponse('잘못된 요청입니다.')


class MypageServiceSettingView(View):
    def get(self,request):
        return render(request, 'mypage/mypage-sevice-settings.html')


class MypageSignOutView(View):
    def get(self, request):
        return render(request, 'mypage/mypage-sign-out.html')

    def post(self, request):  # POST 메서드로 요청 처리
        member_email = request.session.get('member_email')

        # 로그아웃 시 회원 모델 업데이트
        if member_email:
            try:
                member = Member.objects.get(member_email=member_email)
                member.member_status = 'DELETED'  # 또는 다른 원하는 상태로 업데이트
                member.save()
            except Member.DoesNotExist:
                pass

            # Kakao API를 사용하여 로그아웃 처리
            access_token = request.session.get('access_token')
            if access_token:
                headers = {
                    'Authorization': f'Bearer {access_token}',
                    'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
                }
                response = requests.post('https://kapi.kakao.com/v1/user/logout', headers=headers)

            # 세션 비우기
            request.session.clear()

            # 로그아웃 (Django 내장 로그아웃 함수)


        # 메인 페이지로 리디렉션
        return redirect('main:main')




class MemberChangeDonationStatusAPIView(APIView):
    def get(self, request):
        member = Member.objects.get(member_email=request.session.get("member_email"))
        if member.donation_status == "공개":
            member.donation_status = "비공개"
        else:
            member.donation_status = "공개"

        member.save()
        return Response(True)

class TimeReplyTimeView(APIView):
    def get(self, request):
        return render(request, 'mypage/mypage-main.html')


class DonationListAPIView(APIView):
    def get(self, request):
        member_email = request.session.get('member_email')
        page = int(request.GET.get("page"))
        year = request.GET.get('year')

        if not year:
            neulhaerang_dontaion = NeulhaerangDonation.objects.filter(member__member_email=member_email)
        else :
            neulhaerang_dontaion = NeulhaerangDonation.objects.filter(member__member_email=member_email,created_date__year=int(year))
        print(neulhaerang_dontaion)

        pagenator = Pagenation(page=page, page_count=5, row_count=5, query_set=neulhaerang_dontaion)

        donation_list = NeulhaerangDonationSerializer(pagenator.paged_models, many=True).data
        serialized_pagenator = PagenatorSerializer(pagenator).data

        datas = {
            'donation_list':donation_list,
            'serialized_pagenator':serialized_pagenator,

        }
        return JsonResponse(datas)


class MypageGetAthenticationFeedsByPagedAPIView(APIView):
    def get(self, request):
        member_email = request.session.get('member_email')
        page = int(request.GET.get("page"))
        feeds = NeulhajangAuthenticationFeed.objects.filter(member__member_email=member_email).annotate(neulhajang_title=F('neulhajang__neulhajang_title')).values()



        pagenator = Pagenation(page=page, page_count=5, row_count=5, query_set=feeds)

        serialized_pagenator = PagenatorSerializer(pagenator).data


        datas = {
            'feeds':pagenator.paged_models,
            'serialized_pagenator':serialized_pagenator,

        }
        return Response(datas)

class MypageDeleteAthenticationFeedAPIView(APIView):
    def get(self,request):
        feed_id = request.GET.get("feed_id")
        NeulhajangAuthenticationFeed.objects.filter(id=feed_id).delete()

        return Response(True)

class MypageDeleteReplyAPIView(APIView):
    def get(self,request):
        reply_id = request.GET.get("reply_id")
        type = request.GET.get("type")

        if type=="늘해랑":
            NeulhaerangReply.objects.filter(id=reply_id).delete()
        else:
            NeulhaerangReviewReply.objects.filter(id=reply_id).delete()

        return Response(True)


class MypageGetRepliesByPagedAPIView(APIView):
    def get(self,request):
        member_email = request.session.get('member_email')
        page = int(request.GET.get("page"))

        reply_neulhaerang = NeulhaerangReply.objects.filter(member__member_email=member_email, donation__isnull=True).annotate(
            type=Value("늘해랑")).annotate(like_count=Count("replylike")).annotate(title=F("neulhaerang__neulhaerang_title")).values()
        reply_neulhaerang_review = NeulhaerangReviewReply.objects.filter(member__member_email=member_email).annotate(
            type=Value("후기")).annotate(like_count=Count("reviewreplylike")).annotate(title=F("neulhaerang_review__review_title")).values()

        total_reply = list(reply_neulhaerang) + list(reply_neulhaerang_review)
        total_reply_sorted = sorted(total_reply, key=lambda item: item.get("created_date"))
        total_reply_sorted.reverse()

        total_reply_count = (reply_neulhaerang.count() + reply_neulhaerang_review.count())

        pagenator = Pagenation(page=page, page_count=5, row_count=5, query_set=total_reply_sorted)

        serialized_pagenator = PagenatorSerializer(pagenator).data

        datas = {
            'total_reply_sorted': pagenator.paged_models,
            'serialized_pagenator': serialized_pagenator,
        }
        return Response(datas)

class MypageGetByeoljjisByPagedAPIView(APIView):
    def get(self,request):
        member_email = request.session.get('member_email')
        page = int(request.GET.get("page"))

        byeoljjis = Byeoljji.objects.filter(memberbyeoljji__member__member_email=member_email).annotate(review_id=F("neulhaerang__neulhaerangreview")).values()




        pagenator = Pagenation(page=page, page_count=5, row_count=8, query_set=byeoljjis)

        serialized_pagenator = PagenatorSerializer(pagenator).data

        datas = {
            'byeoljjis': list(pagenator.paged_models),
            'serialized_pagenator': serialized_pagenator,
        }
        return Response(datas)

class MypageGetBadgeInfoAPIView(APIView):
    def get(self,request):
        badge_id = int(request.GET.get("badge_id"))
        badge = Badge.objects.filter(id=badge_id).annotate(category_name=F("category__category_name")).values()

        datas={
            "badge":badge.first()
        }
        return JsonResponse(datas)





#작성폼


class MypageNeulhaerangWriteFormView(View):
    def get(self,request):

        return render(request,'mypage/write/neulhaerang-write.html')

    def post(self,request):
        #늘해랑 먼저 크리에이트

        member_email = request.session.get("member_email")
        member = Member.objects.get(member_email=member_email)

        #카테고리
        category = request.POST.get("category")
        category = Category.objects.filter(category_name=category).first()

        #모금 기간
        want_fund_duration = request.POST.get("fundraising_period")

        #봉사기간
        volunteer_start_date = request.POST.get("volunteer_start_date")
        volunteer_start_date = datetime.strptime(volunteer_start_date, "%Y-%m-%d").date()
        volunteer_end_date = request.POST.get("volunteer_end_date")
        volunteer_end_date = datetime.strptime(volunteer_end_date, "%Y-%m-%d").date()



        #참가자 최대인원
        participants_max =request.POST.get("participants_max")

        #목표 미달시 대안
        plan_comment = request.POST.get("plan_comment")

        #관리자한테 할말
        planDetail= request.POST.get("planDetail")

        #제목
        title = request.POST.get("title")
        #썸네일
        thumbnail= request.FILES.get("thumbnail")


        #오픈챗 링크
        openchat_link = request.POST.get("openchat_link")



        plan_moneys = request.POST.getlist("plan_money")

        target_amount = 0
        for money in plan_moneys:
            target_amount+=int(money)




        neulhaerang = Neulhaerang.objects.create(member=member,category=category,neulhaerang_duration=int(want_fund_duration),
                    volunteer_duration_start_date=volunteer_start_date,volunteer_duration_end_date=volunteer_end_date,
                   participants_max_count=participants_max, target_amount_alternatives_plan=plan_comment,
                      message_to_admin=planDetail,neulhaerang_title=title,thumbnail_image=thumbnail,
                       participants_openchat_link=openchat_link,target_amount=target_amount,neulhaerang_status="검토중"
                       )

        # 펀딩 사용 계획
        use_plans = request.POST.getlist("use_plan")
        for i in range(len(use_plans)):
            BusinessPlan.objects.create(neulhaerang=neulhaerang, plan_name=use_plans[i],plan_amount=int(plan_moneys[i]))



        # 소제목
        inner_titles = request.POST.getlist("inner_title")
        inner_title_content_orders =request.POST.getlist("inner_title_content_order")
        for i in range(len(inner_titles)):
            NeulhaerangInnerTitle.objects.create(neulhaerang=neulhaerang,inner_title_text=inner_titles[i],neulhaerang_content_order=int(inner_title_content_orders[i]))

        # #본문
        inner_contents = request.POST.getlist("inner_content")
        inner_content_content_orders = request.POST.getlist("inner_content_content_order")
        for i in range(len(inner_contents)):
            NeulhaerangInnerContent.objects.create(neulhaerang=neulhaerang,inner_content_text=inner_contents[i],neulhaerang_content_order=int(inner_content_content_orders[i]))

        # #태그
        tags = request.POST.getlist("tag")
        for tag in tags :
            NeulhaerangTag.objects.create(neulhaerang=neulhaerang,tag_name=tag,tag_type=random.randint(1, 10))

        # #별찌 이름
        byeoljji_names = request.POST.getlist("byeoljji_name")
         #별찌 인원
        byeoljji_counts = request.POST.getlist("byeoljji_count")
        for i in range(len(byeoljji_names)):
            Byeoljji.objects.create(neulhaerang=neulhaerang,byeoljji_name=byeoljji_names[i],byeoljji_count=int(byeoljji_counts[i]),byeoljji_rank=i+1)


        # #포토텍스트는 무조건 순서대로 10개씩 옴
        photo_texts = request.POST.getlist("caption")
        #
        #
        # #앞에는 컨텐트오더 _ 포토갯수
        inner_photo_content_orders = request.POST.getlist("inner_photo_content_order")
        #
        #
        #
        # #포토는 무조건 순서대로 빈값없이 나옴
        files = request.FILES.getlist("inner_photo")

        photos= []
        content_orders = []
        photo_explanations = []
        count = 0
        text_count =0

        for order in inner_photo_content_orders:
            inner_photo_content_order = int(order.split("_")[0])
            photo_count = int(order.split("_")[1])

            content_orders.append(inner_photo_content_order)
            photos.append(files[count:count+photo_count])
            count+=photo_count
            photo_explanations.append(photo_texts[text_count:text_count+photo_count])
            text_count+=10


        for i in range(len(content_orders)):
            for j in range(len(photos[i])):
                NeulhaerangInnerPhotos.objects.create(neulhaerang=neulhaerang,
                                                      inner_photo=photos[i][j],neulhaerang_content_order=content_orders[i],
                                                      photo_order=j,photo_explanation=photo_explanations[i][j])

        neulhaerang_message = f"늘해랑 제목 : {neulhaerang.neulhaerang_title}에 대한 검토가 진행중입니다.!\n" \
                              f"검토는 최대 15일 걸릴 수 있으며 완료시 알림으로 알려드립니다! \n"

        Alarm.objects.create(message=neulhaerang_message, type="neulhaerang", reference_id=neulhaerang.id,
                             member=neulhaerang.member)



        return redirect(f'/neulhaerang/detail/{neulhaerang.id}')



class getByeoljjiNameAPIView(APIView):
    def get(self,request):
        neulhaerang_id = request.GET.get("neulhaerang_id")
        byeoljjiss = Byeoljji.objects.filter(neulhaerang_id=neulhaerang_id).order_by('byeoljji_rank').values(
            "byeoljji_name")
        datas = {
            "byeoljjiss":list(byeoljjiss)
        }
        return JsonResponse(datas)

class MypageNeulhaerangReviewWriteFormView(View):
    def get(self, request):
        neulhaerang_id = request.GET.get("neulhaerang_id")
        print(neulhaerang_id)
        fund_total = Neulhaerang.objects.filter(id=neulhaerang_id).annotate(fund_total=Sum('neulhaerangdonation__donation_amount')).values().first()
        if fund_total :
            fund_total = fund_total['fund_total']
        else :
            fund_total=0

        datas = {
            "fund_total" : fund_total,
            "neulhaerang_id":neulhaerang_id
        }
        return render(request, 'mypage/write/neulhaerang-review-write.html',datas)

    def post(self,request):
        #늘해랑 먼저 크리에이트

        member_email = request.session.get("member_email")
        member = Member.objects.get(member_email=member_email)

        neulhaerang_id = int(request.POST.get("neulhaerang_id"))


        #제목
        title = request.POST.get("title")
        #썸네일
        thumbnail= request.FILES.get("thumbnail")

        openchat_link = request.POST.get("openchat_link")

        neulhaerang_review= NeulhaerangReview.objects.create(neulhaerang_id=neulhaerang_id,review_title=title,thumbnail_image=thumbnail,byeoljji_receiver_openchat_link=openchat_link)


        historys= request.POST.getlist("history")
        history_moneys = request.POST.getlist("history_money")

        for i in range(len(historys)):
            FundUsageHistory.objects.create(neulhaerang_review=neulhaerang_review,history_name=historys[i],history_amount=int(history_moneys[i]))

        # 소제목
        inner_titles = request.POST.getlist("inner_title")
        inner_title_content_orders =request.POST.getlist("inner_title_content_order")
        for i in range(len(inner_titles)):
            ReviewInnerTitle.objects.create(neulhaerang_review=neulhaerang_review,inner_title_text=inner_titles[i],neulhaerang_content_order=int(inner_title_content_orders[i]))

        # #본문
        inner_contents = request.POST.getlist("inner_content")
        inner_content_content_orders = request.POST.getlist("inner_content_content_order")
        for i in range(len(inner_contents)):
            ReviewInnerContent.objects.create(neulhaerang_review=neulhaerang_review,inner_content_text=inner_contents[i],neulhaerang_content_order=int(inner_content_content_orders[i]))

        # #태그
        tags = request.POST.getlist("tag")
        for tag in tags :
            NeulhaerangReviewTag.objects.create(neulhaerang_review=neulhaerang_review,tag_name=tag,tag_type=random.randint(1, 10))




        # #포토텍스트는 무조건 순서대로 10개씩 옴
        photo_texts = request.POST.getlist("caption")
        #
        #
        # #앞에는 컨텐트오더 _ 포토갯수
        inner_photo_content_orders = request.POST.getlist("inner_photo_content_order")
        #
        #
        #
        # #포토는 무조건 순서대로 빈값없이 나옴
        files = request.FILES.getlist("inner_photo")

        photos= []
        content_orders = []
        photo_explanations = []
        count = 0
        text_count =0

        for order in inner_photo_content_orders:
            inner_photo_content_order = int(order.split("_")[0])
            photo_count = int(order.split("_")[1])

            content_orders.append(inner_photo_content_order)
            photos.append(files[count:count+photo_count])
            count+=photo_count
            photo_explanations.append(photo_texts[text_count:text_count+photo_count])
            text_count+=10
        byeoljjis = Byeoljji.objects.filter(neulhaerang_id=neulhaerang_id).order_by("byeoljji_rank")
        member_donation = NeulhaerangDonation.objects.filter(neulhaerang__neulhaerangreview=neulhaerang_review).values(
            "member").annotate(donation_sum=Sum("donation_amount")).order_by("-donation_sum").values("member")
        tt=0


        byeoljji_files = request.FILES.getlist("byeoljji")
        print(byeoljji_files)
        for i in range(len(byeoljjis)):
            byeoljjis[i].byeoljji_img = byeoljji_files[i]
            byeoljjis[i].save()
            print(byeoljji_files[i])
            count = count + 1
            for j in range(byeoljjis[i].byeoljji_count):
                member_id = member_donation[tt].get("member")
                MemberByeoljji.objects.create(member_id=member_id,byeoljji=byeoljjis[i])
                tt = tt+1





        for i in range(len(content_orders)):
            for j in range(len(photos[i])):
                ReviewInnerPhotos.objects.create(neulhaerang_review=neulhaerang_review,
                                                      inner_photo=photos[i][j],neulhaerang_content_order=content_orders[i],
                                                      photo_order=j,photo_explanation=photo_explanations[i][j])



        review_message = f"늘해랑 리뷰 제목 : {neulhaerang_review.review_title}이(가) 작성되었어요.!\n" \
                              f"얼른 가서 봉사활동 리뷰를 확인해보세요! \n"

        members = Neulhaerang.objects.filter(id=neulhaerang_id).values("neulhaerangparticipants__member_id")
        members2 = Neulhaerang.objects.filter(id=neulhaerang_id).values("neulhaerangdonation__member_id")


        for mem in members:
            print(mem)
            if mem.get("neulhaerangparticipants__member_id") :
                Alarm.objects.create(message=review_message, type="review", reference_id=neulhaerang_review.id,
                                     member_id=mem.get("neulhaerangparticipants__member_id"))


        for memm in members2:
            if memm.get("neulhaerangdonation__member_id"):
                Alarm.objects.create(message=review_message, type="review", reference_id=neulhaerang_review.id,
                                      member_id=memm.get("neulhaerangdonation__member_id"))



        return redirect(f'/neulhaerang_review/review/detail/{neulhaerang_review.id}')







class MypageNeulhajangWriteFormView(View):
    def get(self, request):
        return render(request, 'mypage/write/neulhajang-write.html')


    def post(self,request):
        # 늘하장 먼저 크리에이트

        member_email = request.session.get("member_email")
        member = Member.objects.get(member_email=member_email)

        # 카테고리
        category = request.POST.get("category")
        category = Category.objects.filter(category_name=category).first()

        # 늘하장 기간
        want_fund_duration = request.POST.get("fundraising_period")

        # 공약실천기간
        volunteer_start_date = request.POST.get("volunteer_start_date")
        volunteer_start_date = datetime.strptime(volunteer_start_date, "%Y-%m-%d").date()
        volunteer_end_date = request.POST.get("volunteer_end_date")
        volunteer_end_date = datetime.strptime(volunteer_end_date, "%Y-%m-%d").date()

        # 목표 행동자수
        participants_max = request.POST.get("participants_max")

        # 공약 내용
        commitment_content = request.POST.get("commitment_content")

        # 관리자한테 할말
        planDetail = request.POST.get("planDetail")

        # 제목
        title = request.POST.get("title")
        # 썸네일
        thumbnail = request.FILES.get("thumbnail")

        # 오픈챗 링크
        openchat_link = request.POST.get("openchat_link")

        # #태그
        tag = request.POST.get("tag")


        neulhajang = Neulhajang.objects.create(member=member, category=category,
                                                 neulhajang_duration=int(want_fund_duration),
                                                 commitment_duration_start_date=volunteer_start_date,
                                                 commitment_duration_end_date=volunteer_end_date,
                                                 participants_target_amount=participants_max,
                                                 promise_commit_content=commitment_content,
                                                 message_to_admin=planDetail,
                                               neulhajang_title=title,
                                                 thumnail_image=thumbnail,
                                                 participants_openchat_link=openchat_link, representing_tag=tag,
                                                 neulhajang_status="검토중"
                                                 )

        # 미션 내용
        mission_contents = request.POST.getlist("mission_content")
        for i in range(len(mission_contents)):
            NeulhajangMission.objects.create(neulhajang=neulhajang, mission_content=mission_contents[i],
                                        mission_order=i+1)

        # 소제목
        inner_titles = request.POST.getlist("inner_title")
        inner_title_content_orders = request.POST.getlist("inner_title_content_order")
        for i in range(len(inner_titles)):
            NeulhajangInnerTitle.objects.create(neulhajang=neulhajang, inner_title_text=inner_titles[i],
                                                 neulhajang_content_order=int(inner_title_content_orders[i]))

        # #본문
        inner_contents = request.POST.getlist("inner_content")
        inner_content_content_orders = request.POST.getlist("inner_content_content_order")
        for i in range(len(inner_contents)):
            NeulhajangInnerContent.objects.create(neulhajang=neulhajang, inner_content_text=inner_contents[i],
                                                   neulhajang_content_order=int(inner_content_content_orders[i]))






        photo_texts = request.POST.getlist("caption")

        inner_photo_content_orders = request.POST.getlist("inner_photo_content_order")

        files = request.FILES.getlist("inner_photo")

        for i in range(len(inner_photo_content_orders)):
            NeulhajangInnerPhoto.objects.create(neulhajang=neulhajang,inner_photo=files[i],neulhajang_content_order=int(inner_photo_content_orders[i]),
                                                photo_explanation=photo_texts[i])

        neulhajang_message = f"늘하장 제목 : {neulhajang.neulhajang_title}에 대한 검토가 진행중입니다.!\n" \
                             f"검토는 최대 15일 걸릴 수 있으며 완료시 알림으로 알려드립니다!"
        Alarm.objects.create(message=neulhajang_message, type="neulhajang", reference_id=neulhajang.id,
                             member=neulhajang.member)

        return redirect(f'/neulhajang/detail/{neulhajang.id}')






