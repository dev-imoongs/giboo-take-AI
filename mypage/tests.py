from django.test import TestCase

import neulhaerang
from member.models import Member
from neulhaerang.models import NeulhaerangParticipants, NeulhaerangReply, MemberByeoljji
from neulhaerang_review.models import NeulhaerangReviewReply, NeulhaerangReview
from static_app.models import Badge, MemberBadge


# Create your tests here.
# class MemberTest(TestCase):
#     Member.objects.bulk_create([
#         Member(member_email='test1@gmail.com', member_nickname='테스트1', member_age=30, member_gender='male',  member_role='member', member_status='nomal',
#                ),
#         Member(member_email='test2@naver.com', member_nickname='테스트2', member_age=20, member_gender='male',  member_role='member', member_status='nomal',
#                ),
#         Member(member_email='test3@naver.com', member_nickname='테스트3', member_age=40, member_gender='male',  member_role='member', member_status='nomal'
#                ),
#         Member(member_email='test4@google.com', member_nickname='테스트4', member_age=50, member_gender='male',  member_role='member', member_status='nomal'
#                ),
#         Member(member_email='test5@nate.com', member_nickname='테스트5', member_age=20, member_gender='male',  member_role='admin', member_status='nomal'
#                )
#     ])

# class NeulhaerangParticipants(TestCase):
#     NeulhaerangParticipants.objects.bulk_create([
#         NeulhaerangParticipants(member_id=1, neulhaerang_id=1),
#         NeulhaerangParticipants(member_id=1, neulhaerang_id=2),
#
#     ])

# class NeulhaerangReviewReply(TestCase):
#     NeulhaerangReviewReply.objects.bulk_create([
#         NeulhaerangReviewReply(member_id=1, neulhaerang_review_id=1),
#         NeulhaerangReviewReply(member_id=1, neulhaerang_review_id=2),
#         NeulhaerangReviewReply(member_id=1, neulhaerang_review_id=2),
#         NeulhaerangReviewReply(member_id=1, neulhaerang_review_id=2),
#         NeulhaerangReviewReply(member_id=1, neulhaerang_review_id=2),
#         NeulhaerangReviewReply(member_id=1, neulhaerang_review_id=2),
#         NeulhaerangReviewReply(member_id=1, neulhaerang_review_id=2),
#
#
#     ])

# class NeulhaerangReply(TestCase):
#     NeulhaerangReply.objects.bulk_create([
#         NeulhaerangReply(reply_content='테스트 댓글입니다1', donation_id=, member_id=1, neulhaerang_id=1),
#         NeulhaerangReply(reply_content='테스트 댓글입니다2', donation_id=, member_id=1, neulhaerang_id=2),
#         NeulhaerangReply(reply_content='테스트 댓글입니다3', donation_id=, member_id=1, neulhaerang_id=2),
#         NeulhaerangReply(reply_content='테스트 댓글입니다4', donation_id=, member_id=1, neulhaerang_id=2),
#         NeulhaerangReply(reply_content='테스트 댓글입니다5', donation_id=, member_id=1, neulhaerang_id=2),
#         NeulhaerangReply(reply_content='테스트 댓글입니다6', donation_id=, member_id=1, neulhaerang_id=2),
#         NeulhaerangReply(reply_content='테스트 댓글입니다7', donation_id=, member_id=1, neulhaerang_id=2)
#
#
#     ])

# class NeulhaerangReview(TestCase):
#     NeulhaerangReview.objects.bulk_create([
#         NeulhaerangReview(review_title='테스트1', byeoljji_receiver_openchat_link='testlink', neulhaerang_id=1),
#         NeulhaerangReview(review_title='테스트2', byeoljji_receiver_openchat_link='testlink', neulhaerang_id=2),
#
#     ])

# class Badge(TestCase):
#     Badge.objects.bulk_create([
#         Badge(badge_name='새싹 지킴이', badge_content="우리의 미래가 조금 더 밝아졌어요. '어린이' 프로젝트에 기부해보세요.", badge_image='static/image/badge/child.png', category_id=1),
#         Badge(badge_name='청춘 만만세', badge_content="청년에게 에너지를 충전해주세요.'청년' 프로젝트에 기부해보세요.", badge_image='static/image/badge/teen.png', category_id=2),
#         Badge(badge_name='우먼 파워', badge_content='어린 아이부터 노인까지 모든 세대 여성들의 문제 해결에 동참해보세요.', badge_image='static/image/badge/woman.png', category_id=3),
#         Badge(badge_name='내 나이가 어때서', badge_content="야구도 인생도 9회말부터 '실버세대' 프로젝트에 기부해보세요.", badge_image='static/image/badge/silver.png', category_id=4),
#         Badge(badge_name='장애인의 친구', badge_content="장애인과 함께 세상을 바꾸어요.'장애인' 프로젝트에 기부해보세요.", badge_image='static/image/badge/pwd.png', category_id=5),
#         Badge(badge_name='우리 함께', badge_content="우리가 사는 사회가 조금 더 따뜻해지길!'우리 사회' 프로젝트에 기부해보세요.", badge_image='static/image/badge/social.png', category_id=6),
#         Badge(badge_name='지구촌 촌장님', badge_content='전 지구를 한 마을처럼! 세계의 이슈에 관심을 가져보세요.', badge_image='static/image/badge/earth.png', category_id=7),
#         Badge(badge_name='이웃 사랑꾼', badge_content='우리 이웃이 살아갈 세상이 따뜻해집니다. "어려운 이웃" 프로젝트에 기부해보세요.', badge_image='static/image/badge/neighborhood.png', category_id=8),
#         Badge(badge_name='야생동물의 수호자', badge_content='지금도 한 생명이 멸종되고 있어요. 지구별에서 함께 잘 살 수 없을까요?', badge_image='static/image/badge/animal.png', category_id=9),
#         Badge(badge_name='지구별 수호자', badge_content='자연과 인간은 평화롭게 공존할 수 있어요. "환경" 프로젝트에 기부해보세요.', badge_image='static/image/badge/environment.png', category_id=10),
#
#     ])

# class MemberBadge(TestCase):
#     MemberBadge.objects.bulk_create([
#         MemberBadge(badge_id=3, member_id=1),
#     ])

class MemberByeoljji(TestCase):
    MemberByeoljji.objects.bulk_create([
        MemberByeoljji(member_id=1, neulhaerang_id=1),
    ])