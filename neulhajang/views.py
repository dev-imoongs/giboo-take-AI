from datetime import datetime

from django.conf import settings
from django.core import serializers
from django.db.models import Count, F
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import request
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member
from neulhajang.models import Neulhajang, NeulhajangAuthenticationFeed, NeulhajangMission, NeulhajangInnerTitle, \
    NeulhajangInnerContent, NeulhajangInnerPhoto, NeulhajangLike, AuthenticationFeedLike, NeulhajangCommitment, \
    CommitmentInnerPhotos, CommitmentInnerTitle, CommitmentInnerContent
from workspace.pagenation import Pagenation
from workspace.serializers import PagenatorSerializer, NeulhajangSerializer, AuthenticationFeedSerializer


# Create your views here.


class NeulhajangListView(View):
    def get(self, request):
        if request.GET.get("page") is not None:
            page = request.GET.get("page")
        else :
            page = 1
        total_authentication_feed = NeulhajangAuthenticationFeed.objects.all().count()
        datas = {
            'count':format(total_authentication_feed, ",")
        }
        return render(request,'neulhajang/hajang-list.html', datas)


class NeulhajangListAPIView(APIView):
    def get(self, request):
        page = int(request.GET.get("Page"))
        # 전체
        neulhajang = Neulhajang.objects.filter(neulhajang_status='행동중').order_by('id')

        pagenator = Pagenation(page=page, page_count=5, row_count=7, query_set=neulhajang)
        posts = NeulhajangSerializer(pagenator.paged_models, many=True).data
        serialized_pagenator= PagenatorSerializer(pagenator).data

        existsPost = False
        if(posts):
            existsPost = True

        datas = {
            "posts":posts,
            "pagenator" : serialized_pagenator,
            "existsPost" : existsPost
        }
        return Response(datas)

class NeulhajangDetailView(View):
    def get(self, request, neulhajang_id):
        my_email = request.session.get('member_email')
        post = Neulhajang.objects.get(id=neulhajang_id)
        missions = NeulhajangMission.objects.filter(neulhajang_id=neulhajang_id).order_by('id')
        authentication_feed_count = NeulhajangAuthenticationFeed.objects.filter(neulhajang_id=neulhajang_id).count()
        inner_title_query = NeulhajangInnerTitle.objects.filter(neulhajang_id=neulhajang_id)
        content_query = NeulhajangInnerContent.objects.filter(neulhajang_id=neulhajang_id)
        photo_query = NeulhajangInnerPhoto.objects.filter(neulhajang_id=neulhajang_id)
        bottom_posts = Neulhajang.objects.exclude(id=neulhajang_id).order_by('?')[0:6]
        # 남은 일자 구하기
        end_date = Neulhajang.objects.filter(id=neulhajang_id).values()[0]['neulhajang_duration_end_date']
        if end_date:
            trans_end_date = datetime.combine(end_date, datetime.min.time())
            date_difference = trans_end_date - datetime.now()
            days_difference = date_difference.days
        else:
            days_difference =''

        if(my_email):
            check_my_like = NeulhajangLike.objects.filter(member__member_email=my_email, neulhajang=post)
        else:
            check_my_like = False
        inner_contents = list(inner_title_query) + list(content_query) + list(photo_query)
        sorted_contents = sorted(inner_contents, key=lambda item: item.neulhajang_content_order)

        datas = {
            'period_to_end':days_difference,
            'check_my_like':check_my_like,
            'post':post,
            'neulhajang_id':neulhajang_id,
            'participate_target_amount':post.participants_target_amount,
            'missions':missions,
            'authentication_feed_count':authentication_feed_count,
            'inner_contents': serializers.serialize("json", sorted_contents),
            'bottom_posts':bottom_posts,
        }

        return render(request, 'neulhajang/hajang-detail.html', datas)
    def post(self, request, neulhajang_id):
        my_email = request.session.get('member_email')
        member = Member.objects.get(member_email=my_email)
        file = request.FILES
        datas = request.POST
        NeulhajangAuthenticationFeed.objects.create(feedContent=datas['text-form'], feedPhoto=file.get('upload_file'), member=member, neulhajang_id=neulhajang_id)

        return redirect(f'/neulhajang/detail/{neulhajang_id}/')

class NeulhajangLikeAPIView(APIView):
    def get(self, request):
        neulhajang_id = request.GET.get('neulhajangId')
        my_email = request.session.get('member_email')
        member = Member.objects.get(member_email=my_email)
        check_my_like = NeulhajangLike.objects.filter(member__member_email=my_email)

        if(check_my_like):
            NeulhajangLike.objects.filter(member__member_email=my_email).delete()
        else:
            NeulhajangLike.objects.create(member=member, neulhajang_id=neulhajang_id)

        neulhajang_like_count = NeulhajangLike.objects.filter(neulhajang_id=neulhajang_id).count()

        return Response(neulhajang_like_count)

class AuthenticationFeedListAPIView(APIView):
    def get(self, request):
        neulhajang_id = request.GET.get('neulhajangId')
        authen_feed_images = NeulhajangAuthenticationFeed.objects.filter(neulhajang_id=neulhajang_id).values()[0:30]
        datas = {
            'authen_feed_images': list(authen_feed_images),
        }
        return JsonResponse(datas)

class AuthenticationFeedApplyAPIView(APIView):
    def get(self, request):
        neulhajang_id = request.GET.get('neulhajangId')
        post = Neulhajang.objects.filter(id=neulhajang_id).values()
        participants_count = NeulhajangAuthenticationFeed.objects.filter(neulhajang_id=neulhajang_id).count()
        datas = {
            'post':list(post),
            'participants_count':participants_count
        }

        return JsonResponse(datas)

class NeulhajangActionFeedListAPIView(APIView):
    def get(self, request):
        my_email = request.session.get('member_email')
        neulhajang_id = request.GET.get('neulhajangId')
        page = int(request.GET.get('page'))
        sort = request.GET.get('sort')


        if(sort=='최신순'):
            authen_feed_images = NeulhajangAuthenticationFeed.objects.filter(neulhajang_id=neulhajang_id).order_by('-id')
        else:
            authen_feed_images = NeulhajangAuthenticationFeed.objects.filter(neulhajang_id=neulhajang_id).annotate(my_like=Count('authenticationfeedlike')).order_by('-my_like')
        pagenator = Pagenation(page=page, page_count=5, row_count=30, query_set=authen_feed_images)
        action_images = AuthenticationFeedSerializer(pagenator.paged_models, many=True, context={'request': request}).data
        serialized_pagenator = PagenatorSerializer(pagenator).data
        datas = {
            'serialized_pagenator': serialized_pagenator,
            'action_images': action_images,
        }
        return Response(datas)

class ActionFeedLikeAPIView(APIView):
    def get(self, request):
        my_email = request.session.get('member_email')
        feed_id = int(request.GET.get('feedId'))
        member = Member.objects.get(member_email=my_email)
        check_my_like = AuthenticationFeedLike.objects.filter(authentication_feed_id=feed_id, member=member)

        if(check_my_like):
            AuthenticationFeedLike.objects.filter(authentication_feed_id=feed_id, member=member).delete()
        else:
            AuthenticationFeedLike.objects.create(authentication_feed_id=feed_id, member=member)

        action_feed_like_count = AuthenticationFeedLike.objects.filter(authentication_feed_id=feed_id).count()

        return Response(action_feed_like_count)

class NeulhajangNewsAPIView(APIView):
    def get(self, request):
        neulhajang_id = request.GET.get('neulhajangId')
        commitment = NeulhajangCommitment.objects.filter(neulhajang_id=neulhajang_id)\
            .annotate(writer_profile_image=F('neulhajang__member__profile_image'),
                      writer_profile_choice=F('neulhajang__member__profile_image_choice'),
                      writer_kakao_image=F('neulhajang__member__kakao_profile_image'),
                      member_nickname=F('neulhajang__member__member_nickname')).values()

        commitment_inner_title = CommitmentInnerTitle.objects.filter(neulhajang_id=neulhajang_id)
        commitment_inner_content = CommitmentInnerContent.objects.filter(neulhajang_id=neulhajang_id)
        commitment_inner_photos = CommitmentInnerPhotos.objects.filter(neulhajang_id=neulhajang_id)

        inner_contents = list(commitment_inner_title) + list(commitment_inner_content) + list(commitment_inner_photos)
        sorted_contents = sorted(inner_contents, key=lambda item: item.commitment_content_order)

        datas = {
            'commitment': list(commitment),
            'sorted_contents': serializers.serialize("json",sorted_contents),
        }

        return JsonResponse(datas)

