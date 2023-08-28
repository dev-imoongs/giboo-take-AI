from django.core import serializers
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import request
from rest_framework.response import Response
from rest_framework.views import APIView

from neulhajang.models import Neulhajang, NeulhajangAuthenticationFeed, NeulhajangMission, NeulhajangInnerTitle, \
    NeulhajangInnerContent, NeulhajangInnerPhoto, NeulhajangLike
from workspace.pagenation import Pagenation
from workspace.serializers import PagenatorSerializer, NeulhajangSerializer


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
        neulhajang = Neulhajang.objects.all()

        pagenator = Pagenation(page=page, page_count=5, row_count=7, query_set=neulhajang)
        posts = NeulhajangSerializer(pagenator.paged_models, many=True).data
        serialized_pagenator= PagenatorSerializer(pagenator).data

        datas = {
            "posts":posts,
            "pagenator" : serialized_pagenator
        }
        return Response(datas)

class NeulhajangDetailView(View):
    def get(self, request, neulhajang_id):
        post = Neulhajang.objects.get(id=neulhajang_id)
        missions = NeulhajangMission.objects.filter(neulhajang_id=neulhajang_id).order_by('id')
        authentication_feed_count = NeulhajangAuthenticationFeed.objects.filter(neulhajang_id=neulhajang_id).count()
        inner_title_query = NeulhajangInnerTitle.objects.filter(neulhajang_id=neulhajang_id)
        content_query = NeulhajangInnerContent.objects.filter(neulhajang_id=neulhajang_id)
        photo_query = NeulhajangInnerPhoto.objects.filter(neulhajang_id=neulhajang_id)
        bottom_posts = Neulhajang.objects.exclude(id=neulhajang_id).order_by('-id')[0:6]

        inner_contents = list(inner_title_query) + list(content_query) + list(photo_query)
        sorted_contents = sorted(inner_contents, key=lambda item: item.neulhajang_content_order)

        datas = {
            'post':post,
            'neulhajang_id':neulhajang_id,
            'participate_target_amount':post.participants_target_amount,
            'missions':missions,
            'authentication_feed_count':authentication_feed_count,
            'inner_contents': serializers.serialize("json", sorted_contents),
            'bottom_posts':bottom_posts,
        }

        return render(request, 'neulhajang/hajang-detail.html', datas)

class AuthenticationFeedListAPIView(APIView):
    def get(self, request):
        neulhajang_id = request.GET.get('neulhajangId')
        authen_feed_images = NeulhajangAuthenticationFeed.objects.filter(neulhajang_id=neulhajang_id).values()[0:30]

        datas = {
            'authen_feed_images': list(authen_feed_images),
        }

        return JsonResponse(datas)

class NeulhajangLikeAPIView(APIView):
    def get(self, request):
        neulhajang_id = request.GET.get('neulhajangId')
        neulhajang_like_count = NeulhajangLike.objects.filter(neulhajang_id=neulhajang_id).count()
        print()
        datas={

        }
        return JsonResponse(datas)