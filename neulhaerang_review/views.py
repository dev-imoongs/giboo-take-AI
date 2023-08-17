from django.shortcuts import render
from django.views import View


# Create your views here.
class NeulhaerangReviewDetailView(View):
    def get(self,request):
        return render(request,'neulhaerang/review-detail.html')


class NeulhaerangReviewListView(View):
    def get(self,request):
        return render(request,'neulhaerang/review-list.html')
