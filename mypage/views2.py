from django.core import serializers
from django.db.models import F, Count
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from requests import Response
from rest_framework.views import APIView

from member.models import Member
from neulhaerang.models import Neulhaerang, NeulhaerangDonation, NeulhaerangLike
from neulhajang.models import Neulhajang, NeulhajangAuthenticationFeed, AuthenticationFeedLike, NeulhajangLike
from static_app.models import MemberBadge
from workspace.pagenation import Pagenation
from workspace.serializers import PagenatorSerializer, NeulhajangSerializer


class NewMypagePostListView(View):
    def get(self, request):
        member = Member.objects.get(member_email=request.session['member_email'])
        neulhaerang = Neulhaerang.objects.filter(member=member)
        member_neulhaerang_count =Neulhaerang.objects.filter(member=member).count()
        profile_badge = MemberBadge.objects.filter(member=member)[0:1].get().badge.badge_image
        neulhajang_count = Neulhajang.objects.filter(member=member).count()
        neulhajang_au_count = NeulhajangAuthenticationFeed.objects.filter(member=member).count()
        neulhajang_li_count = AuthenticationFeedLike.objects.filter(member=member).count()
        total_neulhajang_count = neulhajang_count + neulhajang_au_count + neulhajang_li_count
        print(total_neulhajang_count)
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
            'total_neulhajang_count':total_neulhajang_count,

        }
        return render(request, 'mypage/mypage-new-post-list.html', context)

class NewMypageNeulhaerangPostListAPIView(APIView):
    def get(self, request):
        print('늘해랑')
        member_email = request.session.get('member_email')
        print(member_email)
        print('늘해랑 이메일')
        page = int(request.GET.get("page"))
        # 주최한 늘해랑
        member_neulhaerang_list = Neulhaerang.objects.filter(member__member_email=member_email).annotate(member_nickname=F('member__member_nickname')).values()

        # 주최한 늘해랑
        member_neulhaerang_do_list = Neulhaerang.objects.filter(member__member_email=member_email)
        print(member_neulhaerang_do_list)
        # 도네이션 참여한 늘해랑
        member_do_list = Neulhaerang.objects.filter(neulhaerangdonation__member__member_email=member_email).annotate(member_nickname=F('member__member_nickname')).values()
        print(member_do_list)
        print('55555')
        member_pa_list = Neulhaerang.objects.filter(neulhaerangparticipants__member__member_email=member_email).annotate(member_nickname=F('member__member_nickname')).values()
        print(member_pa_list)
        print('이게무야')
        # 응원한 늘해랑
        likes = NeulhaerangLike.objects.filter(member__member_email=member_email)
        print(likes)
        member_likes = Neulhaerang.objects.filter(neulhaeranglike__member__member_email=member_email).annotate(member_nickname=F('member__member_nickname')).values()
        print(member_likes)
        print('123')

        # member_au_count = neulhaerang.objects.filter(member__member_email=member_email).annotate(
        #     neulhaerang_id=F('member__id'))
        # print(member_au_count)
        neulhaerang_count = NeulhaerangDonation.objects.values('neulhaerang').annotate(
            neulhaerang_count=Count('neulhaerang'))
        print(neulhaerang_count)

        # liked_neulhaerangs = [like.neulhaerang for like in likes]
        # liked_neulhaerang_titles = [neulhaerang.neulhaerang_title for neulhaerang in liked_neulhaerangs]
        # print(liked_neulhaerang_titles)
        print('전전')
        total_neulhaerang_list = list(member_neulhaerang_list) + list(member_do_list) + list(
            member_likes) + list(member_pa_list)
        print('전')
        print(total_neulhaerang_list)
        print('후')
        total_neulhaerang_sorted = sorted(total_neulhaerang_list, key=lambda item: item['created_date'])
        total_neulhaerang_sorted.reverse()
        print(total_neulhaerang_sorted)

        print("후후")

        pagenator = Pagenation(page=page, page_count=8, row_count=8, query_set=total_neulhaerang_sorted)
        print(pagenator.paged_models)
        neulhaerang_count_json = list(neulhaerang_count)

        # member_nickname = neulhaerangSerializer(pagenator.paged_models, many=True).data
        serialized_pagenator = PagenatorSerializer(pagenator).data


        datas = {
            # 'member_nickname':member_nickname,
            # 'serialized_pagenator':serialized_pagenator,
            'neulhaerang_posts': pagenator.paged_models,
            'neulhaerang_count_json':neulhaerang_count_json,

        }
        return JsonResponse(datas)






class NewMypageNeulhajangPostListAPIView(APIView):
    def get(self, request):
        member_email = request.session.get('member_email')
        page = int(request.GET.get("page"))
        member_neulhajang_list = Neulhajang.objects.filter(member__member_email=member_email).annotate(member_nickname=F('member__member_nickname')).values()


        member_neulhajang_au_list = NeulhajangAuthenticationFeed.objects.filter(member__member_email=member_email)
        au_list_element = Neulhajang.objects.filter(neulhajangauthenticationfeed__member__member_email=member_email).annotate(member_nickname=F('member__member_nickname')).values()


        likes = NeulhajangLike.objects.filter(member__member_email=member_email)
        member_likes = Neulhajang.objects.filter(neulhajanglike__member__member_email=member_email).annotate(member_nickname=F('member__member_nickname')).values()

        # member_au_count = Neulhajang.objects.filter(member__member_email=member_email).annotate(
        #     neulhajang_id=F('member__id'))
        # print(member_au_count)
        neulhajang_count = NeulhajangAuthenticationFeed.objects.values('neulhajang').annotate(
            neulhajang_count=Count('neulhajang'))

        # liked_neulhajangs = [like.neulhajang for like in likes]
        # liked_neulhajang_titles = [neulhajang.neulhajang_title for neulhajang in liked_neulhajangs]
        # print(liked_neulhajang_titles)
        total_neulhajang_list = list(member_neulhajang_list) + list(au_list_element) + list(
            member_likes)

        total_neulhajang_sorted = sorted(total_neulhajang_list, key=lambda item: item['created_date'])
        total_neulhajang_sorted.reverse()


        pagenator = Pagenation(page=page, page_count=8, row_count=8, query_set=total_neulhajang_sorted)
        neulhajang_count_json = list(neulhajang_count)

        # member_nickname = NeulhajangSerializer(pagenator.paged_models, many=True).data
        serialized_pagenator = PagenatorSerializer(pagenator).data


        datas = {
            # 'member_nickname':member_nickname,
            # 'serialized_pagenator':serialized_pagenator,
            'neulhajang_posts': pagenator.paged_models,
            'neulhajang_count_json':neulhajang_count_json,

        }
        return JsonResponse(datas)





# class NewMypagePostListAPIView(APIView):
#     def get(self, request):
#         member_email = request.session.get('member_email')
#         print(member_email)
#         page = int(request.GET.get("page"))
#         member_neulhajang_list = Neulhajang.objects.filter(member__member_email=member_email)
#         member_neulhajang_au_list = NeulhajangAuthenticationFeed.objects.filter(member__member_email=member_email)
#         print(member_neulhajang_au_list)
#         likes = NeulhajangLike.objects.filter(member__member_email=member_email)
#         print(likes.values())
#
#         liked_neulhajangs = [like.neulhajang for like in likes]
#         liked_neulhajang_titles = [neulhajang.neulhajang_title for neulhajang in liked_neulhajangs]
#
#         print(liked_neulhajang_titles)
#         print('전전')
#         total_neulhajang_list = list(member_neulhajang_list) + list(member_neulhajang_au_list) + list(
#             liked_neulhajangs)
#         print('전')
#         print(total_neulhajang_list)
#         print('후')
#         total_neulhajang_sorted = sorted(total_neulhajang_list, key=lambda item: item.created_date)
#         total_neulhajang_sorted.reverse()
#         print(total_neulhajang_sorted)
#         pagenator = Pagenation(page=page, page_count=5, row_count=5, query_set=total_neulhajang_sorted)
#         print(pagenator.paged_models)
#
#         # 필요한 데이터 추출
#         member_neulhajang_data = [
#             {
#
#                 'created_date': neulhajang.created_date,
#                 # 다른 필드 추가
#             }
#             for neulhajang in member_neulhajang_list
#         ]
#
#         member_neulhajang_au_data = [
#             {
#
#                 'created_date': neulhajang.created_date,
#                 # 다른 필드 추가
#             }
#             for neulhajang in member_neulhajang_au_list
#         ]
#
#         liked_neulhajang_data = [
#             {
#
#                 'created_date': neulhajang.created_date,
#                 # 다른 필드 추가
#             }
#             for neulhajang in liked_neulhajangs
#         ]
#
#         # 데이터를 JSON으로 직렬화
#         json_data = {
#             'member_neulhajang_data': member_neulhajang_data,
#             'member_neulhajang_au_data': member_neulhajang_au_data,
#             'liked_neulhajang_data': liked_neulhajang_data,
#         }
#
#         # member_nickname = NeulhajangSerializer(pagenator.paged_models, many=True).data
#         serialized_pagenator = PagenatorSerializer(pagenator).data
#
#         datas = {
#             # 'member_nickname':member_nickname,
#             # 'serialized_pagenator':serialized_pagenator,
#             'neulhajang_posts': pagenator.paged_models,
#             'json_data': json_data,
#         }
#         return JsonResponse(datas)