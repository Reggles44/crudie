from crudie.models import FooBar
from rest_framework import serializers


class FooBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooBar
        fields = ["id", "foo", "bar"]
