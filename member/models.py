from django.db import models

from workspace.models import Period


# Create your models here.
class Member(Period):

    member_email = models.CharField(max_length=200, null=False, blank=False)
    member_nickname = models.CharField(max_length=50, null=False, blank=False)
    member_age = models.IntegerField(null=False, default=0)
    member_gender = models.CharField(max_length=10, null=False, blank=False)
    member_role = models.CharField(max_length=10, null=False, blank=False, default='MEMBER')
    member_status = models.CharField(max_length=10, null=False, blank=False, default='NORMAL')
    donation_status = models.CharField(max_length=10, null=False, blank=False, default='open')
    total_donation_fund = models.IntegerField(null=False, default=0)
    total_donation_count = models.IntegerField(null=False, default=0)
    donation_level = models.CharField(max_length=50, null=False, blank=False, default='bronze')
    # static 기본이미지가 있고, choice가 유저일때 프로필 이미지가 null이면 기본이미지이다.
    # choice가 유저일떄 프로필 이미지가 있으면 프로필 이미지이다.
    # choice가 카카오면 로그인 할때마다 세션의 member_email랑 프로필 url을 담고, 그것을 사용한다.
    profile_image = models.ImageField(null=True, blank=False, upload_to='member/profile/%Y/%m/%d')
    profile_image_choice = models.CharField(max_length=10, null=False, blank=False, default='user')


    class Meta:
        db_table = 'tbl_member'
        ordering = ["-id"]

