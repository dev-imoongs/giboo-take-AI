from rest_framework import serializers

from member.models import Member
from neulhaerang.models import Neulhaerang


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class NeulhaerangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neulhaerang
        fields = '__all__'


class PagenatorSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'
