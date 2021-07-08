from rest_framework import serializers

from .models import HmisPw, HmisChldDisease, HmisChldImmunzt

class HmisPwSerializer(serializers.ModelSerializer):
    class Meta:
        model = HmisPw
        fields = '__all__'


class HmisCdSerializer(serializers.ModelSerializer):
    class Meta:
        model = HmisChldDisease
        fields = '__all__'


class HmisCiSerializer(serializers.ModelSerializer):
    class Meta:
        model = HmisChldImmunzt
        fields = '__all__'