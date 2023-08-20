from rest_framework import serializers

from member.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
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


