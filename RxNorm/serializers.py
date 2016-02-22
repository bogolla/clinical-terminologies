from rest_framework import serializers
from .models import (
    Rxnatomarchive, Rxnconso, Rxncui, Rxncuichanges,
    Rxndoc, Rxnrel, Rxnsab, Rxnsat, Rxnsty
)


class RxnatomarchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rxnatomarchive


class RxnconsoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rxnconso


class RxncuiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rxncui


class RxncuichangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rxncuichanges


class RxndocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rxndoc


class RxnrelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rxnrel


class RxnsabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rxnsab


class RxnsatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rxnsat


class RxnstySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rxnsty