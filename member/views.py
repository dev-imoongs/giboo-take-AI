import requests
from django.shortcuts import render, redirect
from django.views import View

from member.models import Member


# Create your views here.
# 로그인
class LoginView(View):
    def get(self, request):
        code = request.GET.get("code")
        query_string = '?Content-type: application/x-www-form-urlencoded;charset=utf-8&' \
                       'grant_type=authorization_code&' \
                       'client_id=4026e9a3108be3903a5b5e255d4c1f06&' \
                       'redirect_uri=http://localhost:10000/member/oauth/redirect&' \
                       f'code={code}'

        response = requests.post(f'https://kauth.kakao.com/oauth/token{query_string}')
        access_token = response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }

        response = requests.post('https://kapi.kakao.com/v2/user/me', headers=headers)
        info = response.json().get('kakao_account')
        nickname = info.get('profile').get('nickname')
        thumbnail_image_url = info.get('profile').get('thumbnail_image_url')
        email = info.get('email')
        gender = info.get('gender')
        request.session['member_email'] = email
        request.session['thumbnail_image_url'] = thumbnail_image_url
        request.session['access_token'] = access_token

        member = Member.objects.filter(member_email=email).first()
        if not member:
            Member.objects.create(member_email=email, member_nickname=nickname, member_gender=gender)

        return redirect('member:logined')

class LoginedView(View):
    def get(self, request):
        member = Member.objects.get(member_email=request.session['member_email'])
        context = {'member': member}
        return render(template_name='header/logined-header.html', request=request, context=context)


class LogoutView(View):
    def get(self, request):
        token = request.session['access_token']
        print(token)
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }

        response = requests.post('https://kapi.kakao.com/v1/user/logout', headers=headers)
        print(response.json())

        return redirect('member:main')
