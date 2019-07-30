from rest_framework import serializers,fields
from .models import *


class AdultDataSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AdultDataSet
        fields = ("age",
            "work",
            "fnlwgt",
            "education",
            "education_num",
            "marital_status",
            "occupation",
            "relationship",
            "race",
            "sex",
            "capital_gain",
            "capital_loss",
            "hours_per_week",
            "native_country",
            "salary")
