from django.test import TestCase

from neulhaerang.models import Neulhaerang, NeulhaerangDonation


# Create your tests here.

# class NeulhaerangTest(TestCase):
#     NeulhaerangDonation.objects.bulk_create([
#         NeulhaerangDonation(donation_content='응원합니다', donation_amount=50000, donation_anonymous='Y', member_id=5 ,neulhaerang_id=8),
#         NeulhaerangDonation(donation_content='응원합니다', donation_amount=10000, donation_anonymous='Y', member_id=2 ,neulhaerang_id=7),
#         NeulhaerangDonation(donation_content='응원합니다', donation_amount=5000, donation_anonymous='Y', member_id=1 ,neulhaerang_id=9),
#         NeulhaerangDonation(donation_content='응원합니다', donation_amount=2000, donation_anonymous='Y', member_id=4 ,neulhaerang_id=8),
#         NeulhaerangDonation(donation_content='응원합니다', donation_amount=8000, donation_anonymous='Y', member_id=5 ,neulhaerang_id=8),
#
#     ])