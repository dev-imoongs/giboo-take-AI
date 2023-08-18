import math

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from customer_center.models import Inquery
from member.models import Member
from neulhaerang.models import Neulhaerang
from neulhajang.models import Neulhajang
from notice.models import Notice


# Create your views here.


class Pagenation():
    def __init__(self,page,row_count,obj,page_count):
        self.page =page
        self.row_count =row_count
        self.offset = (page - 1) * row_count
        self.limit = page * row_count
        self.total = obj.objects.all().count()
        self.page_count = page_count
        self.end_page = math.ceil(page / page_count) * page_count
        self.start_page = self.end_page - self.page_count + 1
        self.real_end = math.ceil(self.total / self.row_count)
        self.end_page = real_end if endPage > realEnd else endPage
        pageUnit = (page - 1 // 5) + 1





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



        members = Member.objects.all();
        rowCount= 5
        paged_members = Paginator(members,rowCount).page(page)
        print(paged_members.range)

        return render(request,'admin/member/list.html')



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




