import json
import math
from datetime import timedelta
from django.core.mail import EmailMessage, send_mail
from django.core import serializers
from django.core.paginator import Paginator
from django.db.models import Q, F
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from customer_center.models import Inquery, InqueryResponse, Alarm
from member.models import Member
from neulhaerang.models import Neulhaerang
from neulhaerang_review.models import NeulhaerangReview
from neulhajang.models import Neulhajang
from notice.models import Notice
from workspace.pagenation import Pagenation
from workspace.serializers import MemberSerializer, PagenatorSerializer, NeulhaerangSerializer, NeulhajangSerializer, \
    ReviewSerializer, NoticeSerializer, InquerySerializer


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


class AdminGetNeulhaerangsByPagedAPIView(APIView):
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
        neulhaerangs = Neulhaerang.objects.filter(id__in= neulhaerang_ids).delete()
        return Response(True)




class AdminNeulhaerangDetailView(View):
    def get(self,request):
        neulhaerang_id = request.GET.get("neulhaerang_id")
        page = request.GET.get("page")
        search = request.GET.get("search")
        neulhaerang = Neulhaerang.objects.filter(id=neulhaerang_id)[0]

        datas = {
            "neulhaerang" : neulhaerang,
            "page":page,
            "search":search,
        }

        return render(request,'admin/neulhaerang/detail.html',datas)

    def post(self,request):

        request = request.POST
        reason = request.get("refuse-reason")
        page = request.get("page")
        search = request.get("search")
        neulhaerang_id = request.get("neulhaerang_id")
        neulhaerang = Neulhaerang.objects.get(id=neulhaerang_id)

        print(request)
        if reason:
            neulhaerang.neulhaerang_status = "미선정"
            neulhaerang.rejected_message = reason
            neulhaerang.save()
            neulhaerang_message = f"늘해랑 제목 : {neulhaerang.neulhaerang_title}에 대한 검토가 완료되었습니다.!\n" \
                            f"해당 늘해랑은 미선정 되었습니다. \n" \
                            f"미선정 이유를 글에서 확인하시고 보완해 다시 작성해주세요!"
            Alarm.objects.create(message=neulhaerang_message, type="neulhaerang", reference_id=neulhaerang.id, member=neulhaerang.member)

        else:
            neulhaerang.neulhaerang_status ="모금중"
            neulhaerang.fund_duration_start_date=timezone.now().date()
            neulhaerang.fund_duration_end_date = timezone.now() + timedelta(days=neulhaerang.neulhaerang_duration)
            neulhaerang.save()
            neulhaerang_message = f"늘해랑 제목 : {neulhaerang.neulhaerang_title}에 대한 검토가 완료되었습니다.!\n" \
                                  f"지금 부터 바로 펀딩과 모집이 시작됩니다! \n"

            Alarm.objects.create(message=neulhaerang_message, type="neulhaerang", reference_id=neulhaerang.id,
                                 member=neulhaerang.member)
        next_url = reverse("admin:neulhaerang/list") +f"?page={page}&search={search}"
        return redirect(next_url)




class AdminNeulhajangListView(View):
    def get(self, request):
        if request.GET.get("page"):
            page = int(request.GET.get("page"))
        else:
            page = 1

        if request.GET.get("search"):
            search = request.GET.get("search")
        else:
            search = ''

        datas = {
            "page": page,
            "search": search,
        }
        return render(request, 'admin/neulhajang/list.html', datas)





class AdminGetNeulhajangsByPagedAPIView(APIView):
    def get(self,request):
        page = int(request.GET.get("page"))
        search = request.GET.get("search")


        if search :
           neulhajangs_query_set = Neulhajang.objects.filter(neulhajang_title__contains=search).all()
        else:
            neulhajangs_query_set = Neulhajang.objects.all()

        pagenator = Pagenation(page=page, page_count=5, row_count=10,query_set=neulhajangs_query_set)

        neulhajangs = NeulhajangSerializer(pagenator.paged_models,many=True).data
        serialized_pagenator= PagenatorSerializer(pagenator).data

        datas = {
            "neulhajangs":neulhajangs,
            "pagenator" : serialized_pagenator

        }


        return Response(datas)

class AdminDeleteNeulhajangAPIView(APIView):
    def post(self,request):
        neulhajang_ids = json.loads(request.body).get("neulhajang_ids")
        neulhajang = Neulhajang.objects.filter(id__in= neulhajang_ids).delete()
        return Response(True)



class AdminNeulhajangDetailView(View):
    def get(self, request):
        neulhajang_id = request.GET.get("neulhajang_id")
        page = request.GET.get("page")
        search = request.GET.get("search")
        neulhajang = Neulhajang.objects.filter(id=neulhajang_id)[0]

        datas = {
            "neulhajang": neulhajang,
            "page": page,
            "search": search,
        }

        return render(request, 'admin/neulhajang/detail.html', datas)

    def post(self, request):

        request = request.POST
        reason = request.get("refuse-reason")
        page = request.get("page")
        search = request.get("search")
        neulhajang_id = request.get("neulhajang_id")
        neulhajang = Neulhajang.objects.get(id=neulhajang_id)

        print(request)
        if reason:
            neulhajang.neulhajang_status = "미선정"
            neulhajang.rejected_message = reason
            neulhajang.save()
            neulhajang_message = f"늘해랑 제목 : {neulhajang.neulhajang_title}에 대한 검토가 완료되었습니다.!\n" \
                                  f"해당 늘하장은 미선정 되었습니다. \n" \
                                  f"미선정 이유를 글에서 확인하시고 보완해 다시 작성해주세요!"
            Alarm.objects.create(message=neulhajang_message, type="neulhajang", reference_id=neulhajang.id,
                                 member=neulhajang.member)

        else:
            neulhajang.neulhajang_status = "행동중"
            neulhajang.neulhajang_duration_start_date = timezone.now().date()
            neulhajang.neulhajang_duration_end_date = timezone.now() + timedelta(days=neulhajang.neulhajang_duration)
            neulhajang.save()
            neulhajang_message = f"늘하장 제목 : {neulhajang.neulhajang_title}에 대한 검토가 완료되었습니다.!\n" \
                                 f"지금 부터 참가자들의 행동이 시작됩니다!"
            Alarm.objects.create(message=neulhajang_message, type="neulhajang", reference_id=neulhajang.id,
                                 member=neulhajang.member)
        next_url = reverse("admin:neulhajang/list") + f"?page={page}&search={search}"
        return redirect(next_url)


class AdminReviewListView(View):
    def get(self,request):
        if request.GET.get("page"):
            page = int(request.GET.get("page"))
        else:
            page = 1

        if request.GET.get("search"):
            search = request.GET.get("search")
        else:
            search = ''

        datas = {
            "page": page,
            "search": search,
        }
        return render(request, 'admin/review/list.html', datas)


class AdminGetReviewsByPagedAPIView(APIView):
    def get(self,request):
        page = int(request.GET.get("page"))
        search = request.GET.get("search")


        if search :
           reviews_query_set = NeulhaerangReview.objects.filter(Q(review_title__contains=search)|Q(neulhaerang__neulhaerang_title__contains=search)).all()
        else:
            reviews_query_set = NeulhaerangReview.objects.all()

        pagenator = Pagenation(page=page, page_count=5, row_count=10,query_set=reviews_query_set)

        reviews = ReviewSerializer(pagenator.paged_models,many=True).data
        serialized_pagenator= PagenatorSerializer(pagenator).data

        datas = {
            "reviews":reviews,
            "pagenator" : serialized_pagenator

        }


        return Response(datas)

class AdminDeleteReviewAPIView(APIView):
    def post(self,request):
        review_ids = json.loads(request.body).get("review_ids")
        reviews = NeulhaerangReview.objects.filter(id__in= review_ids).delete()
        return Response(True)




class AdminNoticeListView(View):
    def get(self,request):
        if request.GET.get("page"):
            page = int(request.GET.get("page"))
        else:
            page = 1

        if request.GET.get("search"):
            search = request.GET.get("search")
        else:
            search = ''

        datas = {
            "page": page,
            "search": search,
        }
        return render(request, 'admin/notice/list.html', datas)


class AdminGetNoticesByPagedAPIView(APIView):
    def get(self,request):
        page = int(request.GET.get("page"))
        search = request.GET.get("search")


        if search :
           notices_query_set = Notice.objects.filter(notice_title=search).all()
        else:
            notices_query_set = Notice.objects.all()

        pagenator = Pagenation(page=page, page_count=5, row_count=10,query_set=notices_query_set)

        notices = NoticeSerializer(pagenator.paged_models,many=True).data
        serialized_pagenator= PagenatorSerializer(pagenator).data

        datas = {
            "notices":notices,
            "pagenator" : serialized_pagenator
        }


        return Response(datas)

class AdminDeleteNoticeAPIView(APIView):
    def post(self,request):
        notice_ids = json.loads(request.body).get("notice_ids")
        notices = Notice.objects.filter(id__in= notice_ids).delete()
        return Response(True)







class AdminNoticeWriteView(View):
    def get(self,request):

        return render(request,'admin/notice/write.html')

    def post(self,request):
        files = request.FILES

        title = request.POST.get("title")
        content = request.POST.get("content")
        type = request.POST.get("type")
        status = request.POST.get("status")
        if status :
            status = "FIXED"
        else:
            status = "NORMAL"


        file = files.get("file")
        admin = Member.objects.get(member_email=request.session["member_email"])
        Notice.objects.create(notice_title=title,notice_content=content,notice_image=file,type=type,admin=admin,notice_status=status)


        return redirect("admin:notice/list")


class AdminNoticeDetailView(View):
    def get(self, request):
        notice_id = request.GET.get("notice_id")
        page = request.GET.get("page")
        search = request.GET.get("search")
        notice = Notice.objects.filter(id=notice_id)[0]

        datas = {
            "notice": notice,
            "page": page,
            "search": search,
        }

        return render(request, 'admin/notice/detail.html', datas)

    def post(self, request):

        page = request.POST.get("page")
        search = request.POST.get("search")
        notice_id = request.POST.get("notice_id")

        notice = Notice.objects.get(id=notice_id)

        files = request.FILES

        title = request.POST.get("title")
        content = request.POST.get("content")
        type = request.POST.get("type")
        x_falg = request.POST.get("xFlag")

        file = files.get("file")
        if file:
            notice.notice_image = file
        elif x_falg=="true":
            notice.notice_image=''


        admin = Member.objects.get(member_email=request.session["member_email"])
        notice.notice_title=title
        notice.notice_content=content
        notice.admin=admin
        notice.type=type

        notice.save()

        next_url = reverse("admin:notice/list") + f"?page={page}&search={search}"
        return redirect(next_url)



















class AdminInqueryListView(View):
    def get(self,request):
        if request.GET.get("page"):
            page = int(request.GET.get("page"))
        else:
            page = 1

        if request.GET.get("search"):
            search = request.GET.get("search")
        else:
            search = ''

        datas = {
            "page": page,
            "search": search,
        }
        return render(request, 'admin/inquiry/list.html', datas)


class AdminGetInquerysByPagedAPIView(APIView):
    def get(self,request):
        page = int(request.GET.get("page"))
        search = request.GET.get("search")


        if search :
           inquerys_query_set = Inquery.objects.filter(inquery_title__contains=search).all()
        else:
            inquerys_query_set = Inquery.objects.all()

        pagenator = Pagenation(page=page, page_count=5, row_count=10,query_set=inquerys_query_set)

        inquerys = InquerySerializer(pagenator.paged_models,many=True).data
        serialized_pagenator= PagenatorSerializer(pagenator).data

        datas = {
            "inquerys":inquerys,
            "pagenator" : serialized_pagenator
        }


        return Response(datas)

class AdminDeleteInquerysAPIView(APIView):
    def post(self,request):
        inquery_ids = json.loads(request.body).get("inquery_ids")
        inquerys = Inquery.objects.filter(id__in= inquery_ids).delete()
        return Response(True)



class AdminInqueryDetailView(View):
    def get(self,request):
        inquery_id = request.GET.get("inquery_id")
        page = request.GET.get("page")
        search = request.GET.get("search")
        inquery = Inquery.objects.filter(id=inquery_id).annotate(response_content = F("inqueryresponse__response_content")).values().get()
        datas = {
            "inquery": inquery,
            "page": page,
            "search": search,
        }

        return render(request, 'admin/inquiry/detail.html',datas)

    def post(self,request):
        page = request.POST.get("page")
        search = request.POST.get("search")
        inquery_id = request.POST.get("inquery_id")
        main_url = request.build_absolute_uri().split("admin")[0]+"main/main/"

        inquery = Inquery.objects.get(id=inquery_id)
        response_content = request.POST.get("response_content")
        admin = Member.objects.get(member_email=request.session["member_email"])
        inquery_response = InqueryResponse.objects.create(admin=admin,response_content=response_content,inquery=inquery)
        inquery.response_status="답변완료"
        inquery.save()

        email_title = '기부&테이크 문의내용에 대한 답변 메일입니다!'
        html_message = render_to_string('admin/send_email_template.html', {'inquery': inquery,"response_content":response_content,"main_url":main_url})

        recipient_list = [inquery.member.member_email]

        #알람넣기
        alarm_message = f"문의제목 : {inquery.inquery_title}에 대한 답변이 메일로 도착했습니다!\n" \
                        f"지금 바로 확인해보세요!"
        Alarm.objects.create(message=alarm_message,type="inquery",reference_id=inquery.id,member=inquery.member)


        try:
            send_mail(email_title, message="", recipient_list=recipient_list, html_message=html_message,
                      from_email="service.center.12342@gmail.com")
            next_url = reverse("admin:inquery/list") + f"?page={page}&search={search}"
            return redirect(next_url)
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}", status=500)








