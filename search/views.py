from django.shortcuts import render
from django.views import View


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