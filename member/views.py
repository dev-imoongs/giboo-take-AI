import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member


# Create your views here.
# 로그인
class LoginView(View):
    def get(self, request):
        code = request.GET.get("code")
        path = request.GET.get("state")
        query_string = '?Content-type: application/x-www-form-urlencoded;charset=utf-8&' \
                       'grant_type=authorization_code&' \
                       'client_id=4026e9a3108be3903a5b5e255d4c1f06&' \
                       'redirect_uri=http://localhost:10000/member/login&' \
                       f'code={code}'

        response = requests.post(f'https://kauth.kakao.com/oauth/token{query_string}')
        access_token = response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }

        response = requests.post('https://kapi.kakao.com/v2/user/me', headers=headers)
        info = response.json().get('kakao_account')
        print(info)
        email = info.get('email')
        nickname = email[0:3] + "**"
        kakao_image_url = info.get('profile').get('thumbnail_image_url')
        gender = info.get('gender')
        age = info.get('age')
        request.session['member_email'] = email
        request.session['kakao_image_url'] = kakao_image_url
        request.session['access_token'] = access_token

        member = Member.objects.filter(member_email=email).first()
        if not member:
            member = Member.objects.create(member_email=email, member_nickname=nickname, member_gender=gender, member_age=age)
        request.session['member_status'] = member.member_status

        if member.member_role == 'ADMIN':
            path='/admin/main/'


        return redirect(path)




class LogoutView(View):
    def get(self, request):
        path = request.GET.get("path")
        access_token = request.session['access_token']

        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }

        response = requests.post('https://kapi.kakao.com/v1/user/logout', headers=headers)
        request.session.clear()

        return redirect(path)




class LoginAPIView(APIView):
    def get(self, request):
        email = request.session['member_email']

        member = Member.objects.filter(member_email=email).first()
        # Member.objects.update(member_status=status)
        member.member_status = "NORMAL"
        member.save()

        return Response(True)


