from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from customer_center.models import Inquery, Alarm
from member.models import Member
from workspace.pagenation import Pagenation
from workspace.serializers import AlarmSerializer, PagenatorSerializer


# Create your views here.


class AlarmView(View):
    def get(fself,request):
        return render(request,'customer-center/alarm.html')


class GetAlarmsByPagedAPIView(APIView):
    def get(self,request):
        page = int(request.GET.get("page"))
        all_alarms = Alarm.objects.filter(member__member_email=request.session.get("member_email"))
        alarm_pagenator = Pagenation(row_count=5,page_count=5,page=page,query_set=all_alarms)

        alarms_paged = AlarmSerializer(alarm_pagenator.paged_models,many=True).data
        pagenator = PagenatorSerializer(alarm_pagenator).data

        datas={
            "alarms_paged":alarms_paged,
            "pagenator":pagenator
        }

        return Response(datas)

class ChangeAlarmsIsCheckedAPIView(APIView):
    def get(self,request):
        page = int(request.GET.get("page"))
        all_alarms = Alarm.objects.filter(member__member_email=request.session.get("member_email"))
        alarm_pagenator = Pagenation(row_count=5,page_count=5,page=page,query_set=all_alarms)
        for alarm in alarm_pagenator.paged_models:
            alarm.isChecked="checked"
            alarm.save()
        return Response(True)

class DeleteAllAlarmsAPIView(APIView):
    def get(self,request):
        all_alarms = Alarm.objects.filter(member__member_email=request.session.get("member_email")).delete()

        return Response(True)




class CustomerCenterListView(View):
    def get(self,request):
        return render(request,'customer-center/list.html')




class InqueryWriteView(View):
    def get(self,request):
        return render(request, 'customer-center/inquery-write.html')

    def post(self,request):

        title = request.POST.get("title")
        content = request.POST.get("content")
        member_email = request.session["member_email"]
        member = Member.objects.get(member_email=member_email)
        Inquery.objects.create(inquery_title=title,inquery_content=content,member=member,response_status="답변대기")
        return redirect("main:main")
        


