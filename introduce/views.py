from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from neulhaerang.models import Neulhaerang, NeulhaerangLike, NeulhaerangDonation
from neulhajang.models import Neulhajang, NeulhajangLike
from workspace.models import Period


# Create your views here.
class IntroduceAboutView(View):
    def get(self,request):
        neulhaerang_count  = Neulhaerang.objects.all().count()
        neulhajang_count  = Neulhajang.objects.all().count()
        neulhaerang_like_count  = NeulhaerangLike.objects.all().count()
        neulhajang_like_count  = NeulhajangLike.objects.all().count()
        donation_total = NeulhaerangDonation.objects.aggregate(total = Sum("donation_amount"))["total"]
        project_total = neulhajang_count+neulhaerang_count
        like_total = neulhajang_like_count+neulhaerang_like_count
        average = donation_total//project_total

        datas = {
            "project_total":project_total,
            "donation_total":donation_total,
            "like_total":like_total,
            "average":average,

        }
        return render(request,"introduce/about.html",datas)


class IntroduceGibooSuggestionView(View):
    def get(self,request):
        return render(request,"introduce/giboo-suggestion.html")


class IntroducePartnersView(View):
    def get(self,request):
        return render(request,"introduce/partners.html")

class IntroduceStatisticsView(View):
    def get(self,request):
        return render(request,"introduce/statistics.html")