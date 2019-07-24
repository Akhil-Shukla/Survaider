# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AdultDataSet(models.Model):
    age=models.IntegerField(default=0)
    work=models.CharField(max_length=50)
    fnlwgt=models.IntegerField(default=0)
    education=models.CharField(max_length=50)
    education_num=models.IntegerField(default=0)
    marital_status=models.CharField(max_length=20)
    occupation=models.CharField(max_length=20)
    relationship=models.CharField(max_length=20)
    race=models.CharField(max_length=20)
    sex=models.CharField(max_length=20)
    capital_gain=models.IntegerField(default=0)
    capital_loss=models.IntegerField(default=0)
    hours_per_week=models.IntegerField(default=0)
    native_country=models.CharField(max_length=20)
    salary=models.CharField(max_length=10)


    def getDict(self):
        dict={
            "age":self.age,
            "work":self.work,
            "fnlwgt":self.fnlwgt,
            "education":self.education,
            "education_num":self.education_num,
            "marital_status":self.marital_status,
            "occupation":self.occupation,
            "relationship":self.relationship,
            "race":self.race,
            "sex":self.sex,
            "capital_gain":self.capital_gain,
            "capital_loss":self.capital_loss,
            "hours_per_week":self.hours_per_week,
            "native_country":self.native_country,
            "salary":self.salary
        }
        return dict
