from django.core import serializers
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View

from neulhaerang.models import Neulhaerang, NeulhaerangDonation


# Create your views here.

class NeulhaerangDetailView(View):
    def get(self, request, neulhaerang_id):
        posts = Neulhaerang.objects.all()
        context = {
            'posts':posts,
        }
        return render(request,'neulhaerang/detail.html')


class NeulhaerangListView(View):
    def get(self,request):
        posts = Neulhaerang.objects.all()[0:8]
        donation_list = []
        for post in posts:
            post_donation = NeulhaerangDonation.objects.filter(neulhaerang=post).aggregate(Sum('donation_amount'))
            donation_list.append(post_donation)
        print(type(donation_list))

        combined_data = zip(posts, donation_list)

        context = {
            'posts':serializers.serialize("json",posts),
            'fund_now':donation_list,
            'combined_data':combined_data,
        }
        return render(request,'neulhaerang/list.html', context)
