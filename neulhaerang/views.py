from django.core import serializers
from django.db.models import Sum, F, Count
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member
from neulhaerang.models import Neulhaerang, NeulhaerangDonation, NeulhaerangInnerTitle, NeulhaerangInnerContent, \
    NeulhaerangInnerPhotos, BusinessPlan, NeulhaerangTag, NeulhaerangLike
from workspace.pagenation import Pagenation, Pagenation
from workspace.serializers import NeulhaerangSerializer, PagenatorSerializer

# Create your views here.

class NeulhaerangDetailView(View):
    def get(self, request, neulhaerang_id):

        post = Neulhaerang.objects.get(id=neulhaerang_id)
        business_plan = BusinessPlan.objects.filter(neulhaerang_id=neulhaerang_id).order_by('-created_date')
        tags = NeulhaerangTag.objects.filter(neulhaerang_id=neulhaerang_id).order_by('-created_date')

        inner_title_query = NeulhaerangInnerTitle.objects.filter(neulhaerang_id=neulhaerang_id)
        content_query = NeulhaerangInnerContent.objects.filter(neulhaerang_id=neulhaerang_id)
        photo_query = NeulhaerangInnerPhotos.objects.filter(neulhaerang_id=neulhaerang_id)

        contents = list(inner_title_query) + list(content_query) + list(photo_query)

        sorted_contents = sorted(contents, key=lambda item: item.neulhaerang_content_order)
        target_amount = Neulhaerang.objects.filter(id=neulhaerang_id)
        amount_sum = NeulhaerangDonation.objects.filter(neulhaerang=neulhaerang_id).aggregate(Sum('donation_amount'))
        if(amount_sum['donation_amount__sum'] is None):
            amount_sum = {'donation_amount__sum': 0}

        context = {
            'amount_sum': amount_sum['donation_amount__sum'],
            'target_amount': serializers.serialize("json",target_amount),
            'tags': tags,
            'business_plan': serializers.serialize("json",business_plan),
            'post': post,
            'contents': serializers.serialize("json",sorted_contents),
        }
        return render(request,'neulhaerang/detail.html', context)


class NeulhaerangListView(View):

    def get(self, request):
        if request.GET.get("page") is not None:
            page = request.GET.get("page")
        else :
            page = 1

        return render(request, 'neulhaerang/list.html')
    # def get(self,request):
    #     posts = Neulhaerang.objects.all()[0:8]
    #     donation_list = []
    #     for post in posts:
    #         post_donation = NeulhaerangDonation.objects.filter(neulhaerang=post).aggregate(Sum('donation_amount'))
    #         donation_list.append(post_donation)
    #     print(type(donation_list))
    #


        # combined_data = zip(posts, donation_list)
    #
        # context = {
        #     'posts':serializers.serialize("json",posts),
        #     'fund_now':donation_list,
        #     'combined_data':combined_data,
        # }
    #     return render(request,'neulhaerang/list.html', context)


class NeulhaerangAPIView(APIView):
    def get(self, request):
        page = int(request.GET.get("page"))
        category = request.GET.get("category")
        sort = request.GET.get("sort")

        if(category != '전체'):
            neulhaerang = Neulhaerang.objects.all().filter(category__category_name=category)
        else:
            neulhaerang = Neulhaerang.objects.all()

        if(sort == '추천순'):
            neulhaerang = neulhaerang.annotate(neulhaerang=Count('neulhaeranglike')).order_by('-neulhaerang','-created_date')
        elif(sort == '최신순'):
            neulhaerang = neulhaerang.order_by('-created_date')
        else:
            neulhaerang = neulhaerang.order_by('-fund_duration_end_date','-created_date')

        pagenator = Pagenation(page=page, page_count=5, row_count=8, query_set=neulhaerang)
        posts = NeulhaerangSerializer(pagenator.paged_models, many=True).data
        serialized_pagenator= PagenatorSerializer(pagenator).data

        datas = {
            "posts":posts,
            "pagenator" : serialized_pagenator
        }
        return Response(datas)


class TestView(View):
    def post(self, request):

        NeulhaerangInnerPhotos