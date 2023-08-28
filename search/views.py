import json

from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

import neulhaerang
from neulhaerang.models import NeulhaerangTag, Neulhaerang
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


class ShowTagAPIView(APIView):
    def get(self, request):
        tags = NeulhaerangTag.objects.all().order_by("-id")[:10].values()
        datas = {
            "tags": tags
        }

        return Response(datas)


class ShowCategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all().values()

        datas = {
            "categories": categories
        }
        return Response(datas)


class ShowSearchListOfTagView(View):
    def get(self, request, tag_name):
        tag_posts = Neulhaerang.objects.filter(neulhaerangtag__tag_name=tag_name).values()
        print("태그검색 뷰")
        print(list(tag_posts.values()))

        context = {
            "posts": tag_posts
        }
        return render(request, 'search/search-click.html', context)


class ShowSearchListOfCategoryView(View):
    def get(self, request, category_name):
        category_posts = Neulhaerang.objects.filter(category__category_name=category_name).values()
        print("카테고리검색 뷰")
        print(list(category_posts.values()))

        context = {
            "posts": category_posts
        }
        return render(request, 'search/search-click.html', context)

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


