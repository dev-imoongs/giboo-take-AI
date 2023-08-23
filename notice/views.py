from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from notice.models import Notice
from workspace.pagenation import Pagenation
from workspace.serializers import NoticeSerializer, PagenatorSerializer


# Create your views here.


class NoticeListView(View):
    def get(self,request):
        type = request.GET.get("type")
        if type:
            type=type
        else:
            type="전체"

        datas ={
            "type":type
        }

        return render(request, 'notice/list.html',datas)


class GetNoticesByPagedAPIView(APIView):
    def get(self,request):
        page = int(request.GET.get("page"))
        type = request.GET.get("type")
        print(page)
        print(type)
        if type =="전체":
            notice_all_query_set = Notice.objects.all().order_by("notice_status","-created_date")
        else :
            notice_all_query_set = Notice.objects.filter(type=type).all().order_by("notice_status","-created_date")


        pagenator= Pagenation(page=page,row_count=12,query_set=notice_all_query_set,page_count=10)

        notices = NoticeSerializer(pagenator.paged_models,many=True).data
        serialized_pagenator= PagenatorSerializer(pagenator).data

        datas = {
            "notices":notices,
            "pagenator" : serialized_pagenator

        }

        return Response(datas)


class NoticeDetailView(View):
    def get(self,request):
        notice_id = request.GET.get("notice_id")
        notice = Notice.objects.get(id=notice_id)
        notice_content = notice.notice_content
        datas = {
            "notice_content":notice_content,
            "notice":notice,
            "notice_type":notice.type
        }

        return render(request, 'notice/detail.html',datas)