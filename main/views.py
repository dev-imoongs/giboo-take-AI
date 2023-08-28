from django.db.models import Sum, Count
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView

from neulhaerang.models import NeulhaerangDonation, Neulhaerang, NeulhaerangInnerContent, NeulhaerangTag
from neulhajang.models import Neulhajang, NeulhajangInnerContent


# Create your views here.


class MainView(View):
    def get(self, request):
        total_donation = NeulhaerangDonation.objects.aggregate(total_donation = Sum('donation_amount')).get("total_donation")
        total_donation_count = NeulhaerangDonation.objects.all().count()


        datas ={
            "total_donation":total_donation,
            "total_donation_count":total_donation_count,
        }

        return render(request,'main/main.html',context=datas)

class MainGetNeulhaerangsByPagedRandomAPIView(APIView):
    def get(self,request):
        neulhaerangs = list(Neulhaerang.objects.exclude(neulhaerang_status="종료").annotate(donation_sum = Sum('neulhaerangdonation__donation_amount')).order_by('?').values())[0:6]
        print(neulhaerangs)
        innercontents = []
        tags = []
        for neulhaerang in neulhaerangs:
            print(neulhaerang)
            inner_content = NeulhaerangInnerContent.objects.filter(neulhaerang=neulhaerang.get("id")).first()
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

class MainGetNeulhajangByPagedRandomAPIView(APIView):
    def get(self,request):
        neulhajangs = list(Neulhajang.objects.exclude(neulhajang_status="종료").annotate(feed_sum = Count('neulhajangauthenticationfeed')).order_by('?').values())[0:3]
        innercontents=[]
        for neulhajang in neulhajangs:
            inner_content = NeulhajangInnerContent.objects.filter(neulhajang=neulhajang.get("id")).first()
            if(inner_content):
                innercontents.append(inner_content.inner_content_text)

        datas = {
            "neulhajangs" :neulhajangs,
            "inner_contents" :innercontents,
        }
        return JsonResponse(datas)

class SuggestionChoiceView(View):
    def get(self, request):
        return render(request, 'main/suggestion-choice.html')