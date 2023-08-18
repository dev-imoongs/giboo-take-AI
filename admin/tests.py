from datetime import datetime

from django.test import TestCase

from customer_center.models import Inquery
from member.models import Member
from neulhaerang.models import Neulhaerang
from neulhajang.models import Neulhajang
from notice.models import Notice
from static_app.models import Category


# Create your tests here.

class NoticeTest(TestCase):
    # Member.objects.bulk_create([
    #     Member(member_age=20,member_email='admin',member_status='NORMAL',member_role="ADMIN",member_nickname="admin1",member_gender="M")
    # ])
    admin = Member.objects.get(id=6);

    # for i in range(10):
    #     Notice.objects.create(
    #       notice_content=f"공지사항 내용{i}",notice_title=f"공지사항 제목{i}",type="제안자",admin=admin
    #        )

    member = Member.objects.get(id=1)

    # for i in range(10):
    #     Inquery.objects.create(inquery_content=f"질문내용 {i}",inquery_title=f"질문제목 {i}",member=member)


    # category = Category.objects.get(id=1)
    # for i in range(10):
    #     Neulhaerang.objects.create(member=member,neulhaerang_title=f"늘해랑 제목{i}",volunteer_duration_start_date=datetime.now()
    #                                ,volunteer_duration_end_date=datetime.now(),category=category)

    category = Category.objects.get(id=1)
    for i in range(10):
        Neulhajang.objects.create(member=member, neulhajang_title=f"늘하장 제목{i}",
                                  neulhajang_duration_start_date=datetime.now(),neulhajang_duration_end_date=datetime.now(),
                                  commitment_duration_end_date=datetime.now(),commitment_duration_start_date=datetime.now(),category=category)

    # Category.objects.bulk_create([
    #     Category(category_name="어린이"),
    #     Category(category_name="청년"),
    #     Category(category_name="여성"),
    #     Category(category_name="어르신"),
    #     Category(category_name="장애인"),
    #     Category(category_name="우리사회"),
    #     Category(category_name="지구촌"),
    #     Category(category_name="어려운이웃"),
    #     Category(category_name="동물"),
    #     Category(category_name="환경"),
    # ])




