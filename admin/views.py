from django.shortcuts import render
from django.views import View


# Create your views here.




class AdminMainView(View):
    def get(self,request):
        return render(request, 'admin/main.html')


class AdminInqueryListView(View):
    def get(self,request):
        return render(request,'admin/inquiry/list.html')



class AdminInqueryWriteView(View):
    def get(self,request):
        return render(request,'admin/inquiry/write.html')




class AdminMemberListView(View):
    def get(self,request):
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


