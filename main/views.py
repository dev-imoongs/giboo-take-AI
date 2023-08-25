from django.shortcuts import render, redirect
from django.views import View


# Create your views here.


class MainView(View):
    def get(self, request):
        print(dict(request.session))
        return render(request,'main/main.html')


class SuggestionChoiceView(View):
    def get(self, request):
        return render(request, 'main/suggestion-choice.html')

class TestView(View):
    def get(self, request):
        print('들어오ㅓㅏㅆ음')
        request.session['member_email'] = '담았음'

        return redirect('/main/pretest/')

class TestPreView(View):

    def get(self, request):
        print(request.session.get('member_email'))
        return render(request,'neulhaerang/list.html')