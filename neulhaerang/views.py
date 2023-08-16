from django.shortcuts import render
from django.views import View


# Create your views here.

class NeulhaerangDetailView(View):
    def get(self,request):
        return render(request,'neulhaerang/detail.html')


class NeulhaerangListView(View):
    def get(self,request):
        return render(request,'neulhaerang/list.html')


class NeulhaerangReviewDetailView(View):
    def get(self,request):
        return render(request,'neulhaerang/review-detail.html')


class NeulhaerangReviewListView(View):
    def get(self,request):
        return render(request,'neulhaerang/review-list.html')
