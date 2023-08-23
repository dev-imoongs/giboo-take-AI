from django.db.models import Sum
from rest_framework import serializers

from member.models import Member

from neulhaerang.models import Neulhaerang, NeulhaerangDonation, NeulhaerangReply

from neulhaerang.models import Neulhaerang, NeulhaerangDonation
from neulhaerang_review.models import NeulhaerangReview
from neulhajang.models import Neulhajang
from notice.models import Notice



class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class NeulhaerangSerializer(serializers.ModelSerializer):
    member_nickname = serializers.CharField(source='member.member_nickname', read_only=True)
    donation_amount_sum = serializers.SerializerMethodField(method_name='get_donation_amount_sum',read_only=True)

    def get_donation_amount_sum(self, neulhaerang):
        amount_sum = NeulhaerangDonation.objects.filter(neulhaerang=neulhaerang).aggregate(Sum('donation_amount'))
        return amount_sum['donation_amount__sum']

    class Meta:
        model = Neulhaerang
        fields = '__all__'

class NeulhaerangDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeulhaerangDonation
        fields = '__all__'


class NeulhaerangReplySerializer(serializers.ModelSerializer):
    member_nickname = serializers.CharField(source='member.member_nickname', read_only=True)
    class Meta:
        model = NeulhaerangReply

class NeulhaerangReviewSerializer(serializers.ModelSerializer):
    member_nickname = serializers.CharField(source='neulhaerang.member.member_nickname', read_only=True)
    donation_amount_sum = serializers.SerializerMethodField(method_name='get_donation_amount_sum',read_only=True)

    def get_donation_amount_sum(self, neulhaerangreview):
        amount_sum = NeulhaerangDonation.objects.filter(neulhaerang=neulhaerangreview.neulhaerang_id).aggregate(Sum('donation_amount'))
        return amount_sum['donation_amount__sum']

    class Meta:
        model = NeulhaerangReview
        fields = '__all__'

class NeulhajangSerializer(serializers.ModelSerializer):
    member_nickname = serializers.CharField(source='member.member_nickname', read_only=True)
    class Meta:
        model = Neulhajang
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    member_nickname = serializers.CharField(source='neulhaerang.member.member_nickname', read_only=True)
    neulhaerang_title = serializers.CharField(source='neulhaerang.neulhaerang_title', read_only=True)
    neulhaerang_id = serializers.IntegerField(source='neulhaerang.id', read_only=True)
    class Meta:
        model = NeulhaerangReview
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    member_nickname = serializers.CharField(source='admin.member_nickname', read_only=True)
    class Meta:
        model = Notice
        fields = '__all__'

class PagenatorSerializer(serializers.Serializer):

    has_next = serializers.BooleanField()
    has_prev = serializers.BooleanField()
    total = serializers.IntegerField()
    start_page = serializers.IntegerField()
    end_page = serializers.IntegerField()
    page_count =serializers.IntegerField()
    # "has_next":pagenator.has_next,
    # "has_prev":pagenator.has_prev,
    #  "total":pagenator.total,
    #  "start_page":pagenator.start_page,
    #  "end_page":pagenator.end_page


