from django.urls import path
from django.views.generic.base import TemplateView


app_name = 'alarm'

urlpatterns=[
    path('', TemplateView.as_view(template_name='alarm/alarm.html'), name='alarm'),
]