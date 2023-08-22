from django.test import TestCase

from neulhaerang.models import Neulhaerang, NeulhaerangDonation, NeulhaerangInnerTitle, NeulhaerangInnerContent, \
    NeulhaerangInnerPhotos, BusinessPlan, NeulhaerangTag, NeulhaerangLike, Byeoljji


# Create your tests here.


# class NeulhaerangTest(TestCase):
#     NeulhaerangDonation.objects.bulk_create([
#         NeulhaerangDonation(donation_content='응원합니다', donation_amount=50000, donation_anonymous='Y', member_id=5 ,neulhaerang_id=8),
#         NeulhaerangDonation(donation_content='응원합니다', donation_amount=10000, donation_anonymous='Y', member_id=2 ,neulhaerang_id=7),
#         NeulhaerangDonation(donation_content='응원합니다', donation_amount=5000, donation_anonymous='Y', member_id=1 ,neulhaerang_id=9),
#         NeulhaerangDonation(donation_content='응원합니다', donation_amount=2000, donation_anonymous='Y', member_id=4 ,neulhaerang_id=8),
#         NeulhaerangDonation(donation_content='응원합니다', donation_amount=8000, donation_anonymous='Y', member_id=5 ,neulhaerang_id=8),
#
    # ])
    # NeulhaerangInnerTitle.objects.bulk_create([
    #     NeulhaerangInnerTitle(inner_title_text='소제목1',neulhaerang_content_order=4 ,neulhaerang_id=8),
    # ])
    #
    #
    # NeulhaerangInnerContent.objects.bulk_create([
    #     NeulhaerangInnerContent(inner_content_text='본문1', neulhaerang_content_order=5, neulhaerang_id=8),
    # ])
#
#
    # NeulhaerangInnerPhotos.objects.bulk_create([
    #     NeulhaerangInnerPhotos(inner_photo='/static/image/mypage/giboo__takeLogo_white.png', neulhaerang_content_order=5, photo_order=1,
    #                            photo_explanation='사진에 대한 설명1' ,neulhaerang_id=8),
    #     NeulhaerangInnerPhotos(inner_photo='/static/image/nelhajang_thumbnail01.png', neulhaerang_content_order=5, photo_order=2,
    #                            photo_explanation='사진에 대한 설명2', neulhaerang_id=8),
    #     NeulhaerangInnerPhotos(inner_photo='/static/image/logo2.png', neulhaerang_content_order=5, photo_order=3,
    #                            photo_explanation='사진에 대한 설명3', neulhaerang_id=8),
    #
    # ])
    #
    # BusinessPlan.objects.bulk_create([
    #     BusinessPlan(plan_name='보양식 식재료 6,750원×200명×2회', plan_amount=2700000, neulhaerang_id=8),
    #     BusinessPlan(plan_name='테스트 6,750원×200명×1회', plan_amount=1350000, neulhaerang_id=8),
    #
    # ])
    #     NeulhaerangTag.objects.bulk_create([
    #         NeulhaerangTag(tag_name='힘들어요', tag_type=1, neulhaerang_id=8),
    #         NeulhaerangTag(tag_name='흑흑', tag_type=7, neulhaerang_id=8),
    #         NeulhaerangTag(tag_name='너무너무', tag_type=4, neulhaerang_id=8),
    #         NeulhaerangTag(tag_name='흑흑', tag_type=7, neulhaerang_id=8),
    #
    #     ])

    # NeulhaerangLike.objects.bulk_create([
    #     NeulhaerangLike(member_id=1, neulhaerang_id=1),
    #     NeulhaerangLike(member_id=2, neulhaerang_id=2),
    #     NeulhaerangLike(member_id=3, neulhaerang_id=2),
    #     NeulhaerangLike(member_id=4, neulhaerang_id=3),
    #     NeulhaerangLike(member_id=5, neulhaerang_id=3),
    #     NeulhaerangLike(member_id=6, neulhaerang_id=3),
    #     NeulhaerangLike(member_id=7, neulhaerang_id=4),
    #     NeulhaerangLike(member_id=8, neulhaerang_id=4),
    #     NeulhaerangLike(member_id=1, neulhaerang_id=4),
    #     NeulhaerangLike(member_id=2, neulhaerang_id=4),
    #     NeulhaerangLike(member_id=3, neulhaerang_id=5),
    #     NeulhaerangLike(member_id=4, neulhaerang_id=5),
    #     NeulhaerangLike(member_id=5, neulhaerang_id=5),
    #     NeulhaerangLike(member_id=6, neulhaerang_id=5),
    #     NeulhaerangLike(member_id=7, neulhaerang_id=5),
    #     NeulhaerangLike(member_id=8, neulhaerang_id=7),
    #     NeulhaerangLike(member_id=1, neulhaerang_id=7),
    #     NeulhaerangLike(member_id=2, neulhaerang_id=7),
    #     NeulhaerangLike(member_id=3, neulhaerang_id=7),
    #     NeulhaerangLike(member_id=4, neulhaerang_id=7),
    #     NeulhaerangLike(member_id=5, neulhaerang_id=7),
    #     NeulhaerangLike(member_id=6, neulhaerang_id=8),
    # ])

    # Byeoljji.objects.bulk_create([
    #     Byeoljji(byeoljji_name='별찌이름 1',byeoljji_count=1, byeoljji_rank=1, neulhaerang_id=8),
    #     Byeoljji(byeoljji_name='별찌이름 2', byeoljji_count=10, byeoljji_rank=2, neulhaerang_id=8),
    #     Byeoljji(byeoljji_name='별찌이름 3', byeoljji_count=100, byeoljji_rank=3, neulhaerang_id=8),
    # ])