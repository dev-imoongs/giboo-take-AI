import json
import math

from django.core import serializers
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from customer_center.models import Inquery
from member.models import Member
from neulhaerang.models import Neulhaerang
from neulhajang.models import Neulhajang
from notice.models import Notice
from workspace.pagenation import Pagenation
from workspace.serializers import MemberSerializer, PagenatorSerializer


# Create your views here.






class AdminMainView(View):
    def get(self,request):
        recent_five_members = Member.objects.all()[0:5]
        recent_five_notices = Notice.objects.all()[0:5]
        recent_five_neulhaerangs = Neulhaerang.objects.all()[0:5]
        recent_five_neulhajangs = Neulhajang.objects.all()[0:5]

        datas = {
            'recent_five_members':recent_five_members,
            'recent_five_notices':recent_five_notices,
            'recent_five_neulhaerangs':recent_five_neulhaerangs,
            'recent_five_neulhajangs':recent_five_neulhajangs
                 }
        return render(request, 'admin/main.html',context=datas)



class AdminMemberListView(View):
    def get(self,request):
        if request.GET.get("page") is not None:
            page = request.GET.get("page")
        else :
            page = 1




        return render(request,'admin/member/list.html')



class AdminGetMembersByPagedAPIView(APIView):
    def get(self,request):
        page = int(request.GET.get("page"))
        pagenator = Pagenation(page=page, page_count=5, row_count=10, model=Member)

        members = MemberSerializer(pagenator.paged_models,many=True).data
        serialized_pagenator= PagenatorSerializer(pagenator).data

        datas = {
            "members":members,
            "pagenator" : serialized_pagenator

        }


        return Response(datas)






class AdminNeulhaerangListView(View):
    def get(self,request):
        return render(request,'admin/neulhaerang/list.html')


class AdminNeulhaerangDetailView(View):
    def get(self,request):
        return render(request,'admin/neulhaerang/detail.html')


class AdminNeulhajangListView(View):
    def get(self,request):
        return render(request,'admin/neulhajang/list.html')


class AdminNeulhajangDetailView(View):
    def get(self,request):
        return render(request,'admin/neulhajang/detail.html')



class AdminNoticeListView(View):
    def get(self,request):
        return render(request,'admin/notice/list.html')

class AdminNoticeWriteView(View):
    def get(self,request):
        return render(request,'admin/notice/write.html')

class AdminNoticeUpdateView(View):
    def get(self,request):
        return render(request,'admin/notice/update.html')

class AdminReviewListView(View):
    def get(self,request):
        return render(request,'admin/review/list.html')

class AdminReviewDetailView(View):
    def get(self,request):
        return render(request,'admin/review/detail.html')


class AdminInqueryListView(View):
    def get(self,request):
        return render(request,'admin/inquiry/list.html')



class AdminInqueryWriteView(View):
    def get(self,request):
        return render(request,'admin/inquiry/write.html')




