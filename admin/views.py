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
from workspace.serializers import MemberSerializer, PagenatorSerializer, NeulhaerangSerializer


# Create your views here.





#메인 뷰
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
        return render(request,'admin/member/list.html')



class AdminGetMembersByPagedAPIView(APIView):
    def get(self,request):
        page = int(request.GET.get("page"))
        search = request.GET.get("search")

        if search :
            members_query_set = Member.objects.filter(member_nickname__contains=search).all()
        else:
            members_query_set = Member.objects.all()

        pagenator = Pagenation(page=page, page_count=5, row_count=10,query_set=members_query_set)

        members = MemberSerializer(pagenator.paged_models,many=True).data
        serialized_pagenator= PagenatorSerializer(pagenator).data


        datas = {
            "members":members,
            "pagenator" : serialized_pagenator
        }


        return Response(datas)


class AdminChangeMemberStatusAPIView(APIView):
    def post(self,request):
        member_ids = json.loads(request.body).get("member_ids")
        members = Member.objects.filter(id__in = member_ids)

        for member in members:
            if member.member_status =="DELETED":
                member.member_status = "NORMAL"
                member.save()
            else :
                member.member_status ="DELETED"
                member.save()
        return Response(True)







class AdminNeulhaerangListView(View):
    def get(self,request):
        if request.GET.get("page"):
            page = int(request.GET.get("page"))
        else:
            page = 1

        if request.GET.get("search"):
            search =request.GET.get("search")
        else:
            search=''

        datas={
            "page": page,
            "search": search,
        }
        return render(request,'admin/neulhaerang/list.html',datas)


class AdminGetNeulhearangsByPagedAPIView(APIView):
    def get(self,request):
        page = int(request.GET.get("page"))
        search = request.GET.get("search")


        if search :
           neulhaerangs_query_set = Neulhaerang.objects.filter(neulhaerang_title__contains=search).all()
        else:
            neulhaerangs_query_set = Neulhaerang.objects.all()

        pagenator = Pagenation(page=page, page_count=5, row_count=10,query_set=neulhaerangs_query_set)

        neulhaerangs = NeulhaerangSerializer(pagenator.paged_models,many=True).data
        serialized_pagenator= PagenatorSerializer(pagenator).data

        datas = {
            "neulhaerangs":neulhaerangs,
            "pagenator" : serialized_pagenator

        }


        return Response(datas)


class AdminDeleteNeulhaerangAPIView(APIView):
    def post(self,request):
        neulhaerang_ids = json.loads(request.body).get("neulhaerang_ids")
        print(neulhaerang_ids)
        neulhaerangs = Neulhaerang.objects.filter(id__in= neulhaerang_ids).delete()
        return Response(True)




class AdminNeulhaerangDetailView(View):
    def get(self,request):
        nuelhaerang_id = request.GET.get("nuelhaerang_id")
        page = request.GET.get("page")
        search = request.GET.get("search")
        neulhaerang = Neulhaerang.objects.filter(id=nuelhaerang_id)[0]

        datas = {
            "neulhaerang" : neulhaerang,
            "page":page,
            "search":search,
        }

        return render(request,'admin/neulhaerang/detail.html',datas)


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




