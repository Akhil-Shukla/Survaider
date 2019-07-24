from django.conf.urls import url,include
from .views import *
from django.views.generic import TemplateView
from rest_framework import routers



urlpatterns=[

    # url('', TemplateView.as_view(template_name='index.html'))
    url('^home/', TemplateView.as_view(template_name='home.html')),
    url('^malecount/',countBoy),
    url('^relationship/',relationShipCount),

    url('^alldata/',AdultDataNew.as_view()),


]