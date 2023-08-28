from django.db.models import Count
from django.shortcuts import render
from django.views import View
from rest_framework import request
from rest_framework.response import Response
from rest_framework.views import APIView

from neulhajang.models import Neulhajang, NeulhajangAuthenticationFeed, NeulhajangMission
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
        datas = {
            'post':post,
            'participate_target_amount':post.participants_target_amount,
            'missions':missions,
            'authentication_feed_count':authentication_feed_count,
        }

        return render(request, 'neulhajang/hajang-detail.html', datas)