from django.db.models import Sum, Count
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.serializers import ListSerializer

from neulhaerang.models import Neulhaerang, NeulhaerangLike, NeulhaerangDonation, NeulhaerangParticipants, \
    NeulhaerangReply
from neulhaerang_review.models import NeulhaerangReview, NeulhaerangReviewReply
from neulhajang.models import Neulhajang, NeulhajangLike, NeulhajangAuthenticationFeed
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
        neulhaerang_count = Neulhaerang.objects.all().count()
        neulhajang_count = Neulhajang.objects.all().count()
        neulhaerang_like_count = NeulhaerangLike.objects.all().count()
        neulhajang_like_count = NeulhajangLike.objects.all().count()
        donation_total = NeulhaerangDonation.objects.aggregate(total=Sum("donation_amount"))["total"]
        project_total = neulhajang_count + neulhaerang_count
        like_total = neulhajang_like_count + neulhaerang_like_count
        average = donation_total // project_total

        donation_count = NeulhaerangDonation.objects.all().count()
        reply_count = NeulhaerangReply.objects.all().count() + NeulhaerangReviewReply.objects.all().count()



        authentication_feed_total = NeulhajangAuthenticationFeed.objects.count()
        neulhaerang_participatns = NeulhaerangParticipants.objects.count()

        all_total =donation_count + reply_count+ like_total +authentication_feed_total +neulhaerang_participatns

        datas = {
            "project_total": project_total,
            "donation_total": donation_total,
            "like_total": like_total,
            "average": average,
            "authentication_feed_total": authentication_feed_total,
            "neulhaerang_participatns": neulhaerang_participatns,
            "all_total": all_total,

        }

        return render(request,"introduce/statistics.html",datas)

class IntroduceGetChartsView(View):
    def get(self,request):
        year = int(request.GET.get("year"))
        donation_total_by_category_list = Neulhaerang.objects.filter(created_date__year=year).values("category").annotate(donation_total_by_category =Sum("neulhaerangdonation__donation_amount")).values("donation_total_by_category","category")
        print(donation_total_by_category_list)

        neulhaerang_like_count = NeulhaerangLike.objects.filter(created_date__year=year).all().count()
        neulhajang_like_count = NeulhajangLike.objects.filter(created_date__year=year).all().count()

        like_total = neulhajang_like_count + neulhaerang_like_count
        donation_count = NeulhaerangDonation.objects.filter(created_date__year=year).all().count()

        reply_count = NeulhaerangReply.objects.filter(created_date__year=year).all().count() + NeulhaerangReviewReply.objects.filter(created_date__year=year).all().count()

        authentication_feed_total = NeulhajangAuthenticationFeed.objects.filter(created_date__year=year).count()
        neulhaerang_participatns = NeulhaerangParticipants.objects.filter(created_date__year=year).count()

        participate_all = [donation_count,reply_count,like_total,authentication_feed_total,neulhaerang_participatns]
        top_five_neulhaerang = Neulhaerang.objects.filter(created_date__year=year).annotate(total_donation = Sum("neulhaerangdonation__donation_amount"),donation_count =Count("neulhaerangdonation")).values().order_by("-total_donation","-created_date")[0:5]
        datas = {
            "top_five_neulhaerang":list(top_five_neulhaerang),
            "participate_all":participate_all,
            "donation_total_by_category_list":list(donation_total_by_category_list)
        }


        return JsonResponse(datas)


