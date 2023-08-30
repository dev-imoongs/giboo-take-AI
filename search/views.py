import json

from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

import neulhaerang
from neulhaerang.models import NeulhaerangTag, Neulhaerang, NeulhaerangDonation, NeulhaerangParticipants
from neulhajang.models import Neulhajang
from static_app.models import Category


# Create your views here.


class SearchFormView(View):
    def get(self,request):
        return render(request, 'search/search-form.html')

class SearchClickView(View):
    def get(self, request):
        if request.GET.get("page") is not None:
            page = request.GET.get("page")
        else:
            page = 1
        return render(request, 'search/search-click.html')


class SearchInputView(View):
    def get(self,request):
        return render(request, 'search/search-input.html')



# 최신태그 가져오기
class ShowTagAPIView(APIView):
    def get(self, request):
        tags = NeulhaerangTag.objects.all().order_by("-id")[:10].values()
        datas = {
            "tags": tags
        }

        return Response(datas)


# 카테고리 가져오기
class ShowCategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all().values()

        datas = {
            "categories": categories
        }
        return Response(datas)


# 태그 검색 결과페이지로 이동하기
class ShowSearchListOfTagView(View):
    def get(self, request, tag_name, tag_type):
        posts = Neulhaerang.objects.filter(neulhaerangtag__tag_name=tag_name).values()
        amount = NeulhaerangDonation.objects.filter(neulhaerang__neulhaerangtag__tag_name=tag_name).aggregate(Sum('donation_amount'))['donation_amount__sum']
        participants = NeulhaerangParticipants.objects.filter(neulhaerang__neulhaerangtag__tag_name=tag_name).count()
        print("태그검색 뷰")
        print(list(posts))
        print(amount)
        print(participants)

        datas = {
            "tag": tag_name,
            "type": tag_type,
            "amount": '{:,}'.format(amount),
            "participants": '{:,}'.format(participants),
            "posts": posts
        }
        return render(request, 'search/search-click.html', datas)


# 태그 검색 결과 리스트 API View
class ShowSearchListOfTagAPIView(APIView):
    def get(self, request, tag_name):
        pass



# 카테고리 검색결과 페이지로 이동하기
class ShowSearchListOfCategoryView(View):
    def get(self, request, category_name):
        amount = NeulhaerangDonation.objects.filter(neulhaerang__category__category_name=category_name).aggregate(Sum('donation_amount'))['donation_amount__sum']
        participants = NeulhaerangParticipants.objects.filter(neulhaerang__category__category_name=category_name).count()
        category_posts = Neulhaerang.objects.filter(category__category_name=category_name).values()
        print("카테고리검색 뷰")
        print(list(category_posts.values()))

        context = {
            "category_name": category_name,
            "amount": '{:,}'.format(amount),
            "participants": '{:,}'.format(participants),
        }
        return render(request, 'search/search-category.html', context)


# 카테고리 검색결과 리스트 API View
class ShowSearchListOfCategoryAPIView(APIView):
    def get(self, request, category_name):
        print("카테고리 검색결과 리스트 뷰")
        posts = NeulhaerangTag.objects.filter(neulhaerang__category__category_name=category_name).values()
        print(list(posts.values()))
        datas = {
            "category_name": category_name,
            "posts": posts
        }

        return Response(datas)


# 키워드 검색결과 페이지로 이동하기
class ShowSearchListOfKeywordView(View):
    def get(self, request, *args, **kwargs):
        keyword = request.GET.get('keyword')
        neulhaerang_keyword_posts = Neulhaerang.objects.filter(neulhaerang_title__icontains=keyword)
        neulhajang_keyword_posts = Neulhajang.objects.filter(neulhajang_title__icontains=keyword)
        tag_keyword_posts = Neulhaerang.objects.filter(neulhaerangtag__tag_name__icontains=keyword)

        print("키워드 검색 뷰")
        print(list(neulhaerang_keyword_posts.values()))
        print(list(neulhajang_keyword_posts.values()))
        print(list(tag_keyword_posts.values()))

        context = {
            "keyword": keyword,
            "neulhaerangs": neulhaerang_keyword_posts,
            "neulhajangs": neulhajang_keyword_posts,
            "tags": tag_keyword_posts
        }

        return render(request, 'search/search-input.html', context)
