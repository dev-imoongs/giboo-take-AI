from datetime import datetime

from django.db.models import Sum, Count
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member
from neulhaerang.models import NeulhaerangDonation, Neulhaerang, NeulhaerangInnerContent, NeulhaerangTag
from neulhaerang_review.models import NeulhaerangReview, ReviewInnerContent
from neulhajang.models import Neulhajang, NeulhajangInnerContent


# Create your views here.


class MainView(View):
    def get(self, request):
        total_donation = NeulhaerangDonation.objects.aggregate(total_donation = Sum('donation_amount')).get("total_donation")
        total_donation_count = NeulhaerangDonation.objects.all().count()
        now = datetime.now()

        if total_donation:
            total_donation =format(total_donation,",")



        datas ={
            "total_donation":total_donation,
            "total_donation_count":total_donation_count,
            "now":now,
        }

        return render(request,'main/main.html',context=datas)

class MainGetNeulhaerangsByPagedRandomAPIView(APIView):
    def get(self,request):
        neulhaerangs = list(Neulhaerang.objects.filter(neulhaerang_status="모금중").annotate(donation_sum = Sum('neulhaerangdonation__donation_amount')).order_by('?').values())[0:6]
        innercontents = []
        tags = []
        for neulhaerang in neulhaerangs:
            inner_content = NeulhaerangInnerContent.objects.filter(neulhaerang=neulhaerang.get("id")).last()
            if(inner_content):
                innercontents.append(inner_content.inner_content_text)
            tag = NeulhaerangTag.objects.filter(neulhaerang=neulhaerang.get("id")).order_by('?')
            if tag:
                tags.append(tag.first().tag_name)

        datas = {
            "neulhaerangs" :neulhaerangs,
            "inner_contents" :innercontents,
            "tags" :tags,
        }
        return JsonResponse(datas)
class MainGetNeulhaerangReviewSlideAPIView(APIView):
    def get(self,request):
        reviews = list(NeulhaerangReview.objects.order_by('?').values())[0:3]
        innercontents = []
        for review in reviews:
            inner_content = ReviewInnerContent.objects.filter(neulhaerang_review=review.get("id")).last()
            if (inner_content):
                innercontents.append(inner_content.inner_content_text)
        datas = {
            "innercontents":innercontents,
            "reviews" :reviews,

        }
        return JsonResponse(datas)

class MainGetNeulhajangByPagedRandomAPIView(APIView):
    def get(self,request):
        neulhajangs = list(Neulhajang.objects.filter(neulhajang_status="행동중").annotate(feed_sum = Count('neulhajangauthenticationfeed')).order_by('?').values())[0:3]
        innercontents=[]
        for neulhajang in neulhajangs:
            inner_content = NeulhajangInnerContent.objects.filter(neulhajang=neulhajang.get("id")).last()
            if(inner_content):
                innercontents.append(inner_content.inner_content_text)

        datas = {
            "neulhajangs" :neulhajangs,
            "inner_contents" :innercontents,
        }
        return JsonResponse(datas)



class MainGetTagNeulhaerangsRandomAPIView(APIView):
    def get(self,request):
        random_tags =  NeulhaerangTag.objects.filter(neulhaerang__neulhaerang_status="모금중").values("tag_name").annotate(tag_count=Count("tag_name")).values("tag_name","tag_count").order_by("?")[0:4]
        datas={
            "random_tags":list(random_tags)
        }
        return JsonResponse(datas)



class MainGetTagClickNeulhaerangsRandomAPIView(APIView):
    def get(self,request):
        tag = request.GET.get("tag")
        print(tag)
        random_neulhaerangs = Neulhaerang.objects.filter(neulhaerangtag__tag_name=tag,neulhaerang_status="모금중").annotate(donation_sum=Sum("neulhaerangdonation__donation_amount")).values().order_by('?')[0:4]

        datas ={
            "random_neulhaerangs":list(random_neulhaerangs)
        }
        return JsonResponse(datas)


class MainGetOneRandomNeulhaerangByTagAPIView(APIView):
    def get(self,request):
        tag_name= request.GET.get("tag")
        neulhaerang= Neulhaerang.objects.filter(neulhaerangtag__tag_name=tag_name).order_by('?')
        if(neulhaerang):
            neulhaerang_id = neulhaerang.first().id
        else:
            neulhaerang_id = ''
        return Response(neulhaerang_id)


class MainGetMemberRankingAPIView(APIView):
    def get(self,request):
        members = Member.objects.filter(donation_status="공개").annotate(donation_sum = Sum("neulhaerangdonation__donation_amount")).filter(donation_sum__gt=100).order_by('-donation_sum').values()[0:4]
        print(members)
        datas={
            "members" : list(members)
        }
        return JsonResponse(datas)

class SuggestionChoiceView(View):
    def get(self, request):
        return render(request, 'main/suggestion-choice.html')