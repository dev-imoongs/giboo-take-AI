from django.shortcuts import render, redirect
from django.views import View

from customer_center.models import Inquery
from member.models import Member


# Create your views here.


class AlarmView(View):
    def get(self,request):
        return render(request,'customer-center/alarm.html')



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
        


