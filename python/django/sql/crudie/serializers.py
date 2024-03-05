from crudie.models import Crudie
from rest_framework import serializers


class CrudieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crudie
        fields = "__all__"
