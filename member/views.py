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
                       'client_id=82730a86e5659b6ad4023759851f9f34&' \
                       'redirect_uri=http://localhost:10000/member/oauth/redirect&' \
                       f'code={code}'
        print(code)
        print(query_string)

        response = requests.post(f'https://kauth.kakao.com/oauth/token{query_string}')
        print(response)
        access_token = response.json().get('access_token')

        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }

        response = requests.post('https://kapi.kakao.com/v2/user/me', headers=headers)
        print(response.json())
        info = response.json().get('kakao_account')
        nickname = info.get('profile').get('nickname')
        thumbnail_image_url = info.get('profile').get('thumbnail_image_url')
        email = info.get('email')
        request.session['member_email'] = email
        request.session['thumbnail_image_url'] = thumbnail_image_url

        member = Member.objects.filter(member_email=email).first()
        if not member:
            Member.objects.create(member_email=email, member_name=nickname)

        return redirect('member:mypage')

class MyPageView(View):
    def get(self, request):
        member = Member.objects.get(member_email=request.session['member_email'])
        context = {'member': member}
        return render(template_name='mypage/mypage-profile.html', request=request, context=context)