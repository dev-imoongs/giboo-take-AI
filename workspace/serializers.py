from rest_framework import serializers

from member.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'



class PagenatorSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'
