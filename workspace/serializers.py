from django.db.models import Sum
from rest_framework import serializers

from member.models import Member
from neulhaerang.models import Neulhaerang, NeulhaerangDonation


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class NeulhaerangSerializer(serializers.ModelSerializer):
    member_nickname = serializers.CharField(source='member.member_nickname', read_only=True)
    donation_amount_sum = serializers.SerializerMethodField(read_only=True)

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


