from django.shortcuts import render
from django.views import View


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