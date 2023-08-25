from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView

from customer_center.models import Inquery, Alram
from member.models import Member


# Create your views here.


class AlarmView(View):
    def get(fself,request):
        return render(request,'customer-center/alarm.html')


class GetAlarmsByPagedAPIView(APIView):
    def get(self,request):
        page = int(request.GET.get("page"))
        member = Member.objects.get(member_email=request.session.get("member_email"))
        all_alarms = Alram.objects.filter(member=member).values()
        print(all_alarms)



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
        


