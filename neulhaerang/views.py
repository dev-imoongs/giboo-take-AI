from django.core import serializers
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from neulhaerang.models import Neulhaerang, NeulhaerangDonation
from workspace.pagenation import Pagenation
from workspace.serializers import NeulhaerangSerializer, PagenatorSerializer


# Create your views here.

class NeulhaerangDetailView(View):
    def get(self, request, neulhaerang_id):
        posts = Neulhaerang.objects.all()
        context = {
            'posts':posts,
        }
        return render(request,'neulhaerang/detail.html')


class NeulhaerangListView(View):
    def get(self, request):
        return render(request, 'neulhaerang/list.html')
    # def get(self,request):
    #     posts = Neulhaerang.objects.all()[0:8]
    #     donation_list = []
    #     for post in posts:
    #         post_donation = NeulhaerangDonation.objects.filter(neulhaerang=post).aggregate(Sum('donation_amount'))
    #         donation_list.append(post_donation)
    #     print(type(donation_list))
    #
    #     combined_data = zip(posts, donation_list)
    #
    #     context = {
    #         'posts':serializers.serialize("json",posts),
    #         'fund_now':donation_list,
    #         'combined_data':combined_data,
    #     }
    #     return render(request,'neulhaerang/list.html', context)


class NeulhaerangAPIView(APIView):
    def get(self, request):
        page = int(request.GET.get("page"))
        pagenator = Pagenation(page=page, page_count=5, row_count=8, model=Neulhaerang)
        posts = NeulhaerangSerializer(pagenator.paged_models,many=True).data
        serialized_pagenator= PagenatorSerializer(pagenator).data

        datas = {
            "posts":posts,
           # "has_next":pagenator.has_next,
           # "has_prev":pagenator.has_prev,
           #  "total":pagenator.total,
           #  "start_page":pagenator.start_page,
           #  "end_page":pagenator.end_page
            "pagenator" : serialized_pagenator
        }
        return Response(datas)
