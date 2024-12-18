import requests
import environ
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from customer_center.models import Alarm
from member.models import Member
from workspace.serializers import MemberSerializer

env = environ.Env()
environ.Env.read_env()
REST_API_KEY = env('REST_API_KEY')
REDIRECT_URI = 'http://localhost:8000/member/callback/'


# Create your views here.
# 로그인
class LoginView(View):
    def get(self, request):

        if(request.GET.get("path")):
            prev_url = request.GET.get("path")
            request.session["prev_url"] = prev_url

        if 'code' not in request.GET:
            # 1. 인가코드 받기
            uri = f'https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}'
            return redirect(uri)
        else:
            # 2. 토큰 받기
            code = request.GET.get("code")
            prev_url = request.session.get("prev_url")
            query_string = '?Content-type: application/x-www-form-urlencoded;charset=utf-8&' \
                           'grant_type=authorization_code&' \
                           f'client_id={REST_API_KEY}&' \
                           f'redirect_uri={REDIRECT_URI}&' \
                           f'code={code}'
            response = requests.post(f'https://kauth.kakao.com/oauth/token{query_string}')
            access_token = response.json().get('access_token')
            refresh_token = response.json().get('refresh_token')

            # 3. 사용자 정보 가져오기
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
            }
            response = requests.post('https://kapi.kakao.com/v2/user/me', headers=headers)
            info = response.json().get('kakao_account')
            email = info.get('email')
            nickname = email[0:3] + "**"
            kakao_image_url = info.get('profile').get('thumbnail_image_url')
            gender = info.get('gender')
            age = info.get('age')
            request.session['member_email'] = email
            request.session['kakao_image_url'] = kakao_image_url
            request.session['access_token'] = access_token

            if not gender:
                gender = "선택 안함"

            if not age :
                age = 0

            member = Member.objects.filter(member_email=email).first()
            if not member:
                member = Member.objects.create(member_email=email, member_nickname=nickname, member_gender=gender, member_age=age)
            else:
                if member.profile_image_choice=="kakao":
                    member.profile_image=kakao_image_url

            member.save()
            request.session['member_status'] = member.member_status

            go_to_prev = request.session.get("prev_url")
            if member.member_role == 'ADMIN':
                go_to_prev= '/admin/main/'

        return redirect(go_to_prev)

class GetMemberProfileAPIView(APIView):
    def get(self,request):
        member = Member.objects.filter(member_email=request.session.get("member_email")).values().first()
        data ={
            "member": member,
        }
        return JsonResponse(data)

class GetMemberAlarmsNotChckedAPIView(APIView):
    def get(self,request):
        not_checked_alarms_count = Alarm.objects.filter(member__member_email=request.session.get("member_email"),isChecked='').count()
        data ={
            "not_checked_alarms_count": not_checked_alarms_count
        }
        return JsonResponse(data)




class LogoutView(View):
    def get(self, request):
        prev_url = request.GET.get("path")
        print('로그아웃뷰', prev_url)
        if prev_url.split("/")[1] == "mypage":
            prev_url = "/main/main"
        access_token = request.session['access_token']

        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }

        response = requests.post('https://kapi.kakao.com/v1/user/logout', headers=headers)
        request.session.clear()
        return redirect(prev_url)




class LoginAPIView(APIView):
    def get(self, request):
        email = request.session['member_email']

        member = Member.objects.filter(member_email=email).first()
        # Member.objects.update(member_status=status)
        member.member_status = "NORMAL"
        member.save()
        request.session['member_status'] = member.member_status

        return Response(True)
