import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from customer_center.models import Alarm
from member.models import Member
from workspace.serializers import MemberSerializer


# Create your views here.
# 로그인
class LoginView(View):
    def get(self, request):
        code = request.GET.get("code")
        prev_url = request.GET.get("state")
        query_string = '?Content-type: application/x-www-form-urlencoded;charset=utf-8&' \
                       'grant_type=authorization_code&' \
                       'client_id=4026e9a3108be3903a5b5e255d4c1f06&' \
                       'redirect_uri=http://www.giboontake.site/member/login&' \
                       f'code={code}'


        response = requests.post(f'https://kauth.kakao.com/oauth/token{query_string}')
        access_token = response.json().get('access_token')
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

        go_to_prev = prev_url

        if member.member_role == 'ADMIN':
            go_to_prev= '/admin/main/'



        return redirect("/main/main")

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
        print(prev_url)
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


