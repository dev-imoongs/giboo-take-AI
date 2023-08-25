import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from neulhaerang.models import NeulhaerangTag
from static_app.models import Category


# Create your views here.


class SearchFormView(View):
    def get(self,request):
        return render(request, 'search/search-form.html')

class SearchClickView(View):
    def get(self,request):
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