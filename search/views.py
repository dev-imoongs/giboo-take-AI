from django.shortcuts import render
from django.views import View
from static_app.models import Category

# Create your views here.


class SearchFormView(View):
    def get(self,request):
        return render(request, 'search/search-form.html')

class SearchClickView(View):
    def get(self,request, category_name):
        category = Category.objects.get(category_name=category_name)

        return render(request, 'search/search-click.html')


class SearchInputView(View):
    def get(self,request):
        return render(request, 'search/search-input.html')


class ShowTagAPIView(View):
    def get(self,request):
        tags =