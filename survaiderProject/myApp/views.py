# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import csv
from .models import AdultDataSet
from django.http import JsonResponse,HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import viewsets, generics
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.





def countBoy(request):
    boy=AdultDataSet.objects.filter(sex=" Male").count()
    girl=AdultDataSet.objects.filter(sex=" Female").count()
    obj1=json.dumps(boy,
            sort_keys=True,
            indent=1,
            cls=DjangoJSONEncoder)
    obj2=json.dumps(girl,
            sort_keys=True,
            indent=1,
            cls=DjangoJSONEncoder)
    di={}
    di['malecount']=obj1
    di['femalecount']=obj2
    return JsonResponse(di)

def relationShipCount(request):

    not_in_family=AdultDataSet.objects.filter(relationship=" Not-in-family").count()
    husband=AdultDataSet.objects.filter(relationship=" Husband").count()
    wife=AdultDataSet.objects.filter(relationship=" Wife").count()
    own_child=AdultDataSet.objects.filter(relationship=" Own-child").count()
    unmarried=AdultDataSet.objects.filter(relationship=" Unmarried").count()
    di={}
    di['not_in_family'] = json.dumps(not_in_family,cls=DjangoJSONEncoder)
    di['husband'] = json.dumps(husband, cls=DjangoJSONEncoder)
    di['wife'] = json.dumps(wife, cls=DjangoJSONEncoder)
    di['own_child'] = json.dumps(own_child, cls=DjangoJSONEncoder)
    di['unmarried'] = json.dumps(unmarried, cls=DjangoJSONEncoder)
    return JsonResponse(di)



class AdultDataNew(APIView):

    def get(self,request):
        query=AdultDataSet.objects.all()
        serial=AdultDataSerializer(query,many=True)
        return Response(serial.data)





