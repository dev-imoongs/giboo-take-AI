from django.test import TestCase

import neulhaerang
from member.models import Member
from neulhaerang.models import NeulhaerangParticipants, NeulhaerangReply
from neulhaerang_review.models import NeulhaerangReviewReply, NeulhaerangReview


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