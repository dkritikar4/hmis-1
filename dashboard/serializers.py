from rest_framework import serializers

from .models import HmisStatePw, HmisStChldDisease, HmisStChldImmunzt

class HmisStatePwSerializer(serializers.ModelSerializer):
    class Meta:
        model = HmisStatePw
        fields = '__all__'


class HmisStCdSerializer(serializers.ModelSerializer):
    class Meta:
        model = HmisStChldDisease
        fields = '__all__'


class HmisStCiSerializer(serializers.ModelSerializer):
    class Meta:
        model = HmisStChldImmunzt
        fields = '__all__'