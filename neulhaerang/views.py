from django.shortcuts import render
from django.views import View


# Create your views here.

class NeulhaerangDetailView(View):
    def get(self,request):
        return render(request,'neulhaerang/detail.html')


class NeulhaerangListView(View):
    def get(self,request):
        return render(request,'neulhaerang/list.html')


