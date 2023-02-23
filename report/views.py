from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from .models import ModuleData2
import json
from decimal import Decimal

status= [
    { "title": "누적 발전량", "value": "3,000", "unit": "MWh", "icon_class": "fas fa-solar-panel fa-fw" },
    { "title": "최대 발전량", "value": "1,234", "unit": "MWh", "icon_class": "fas fa-bolt" },
    { "title": "발전 최적 시간대", "value": "11 ~ 15", "unit": "시", "icon_class": "fas fa-stopwatch" },
    { "title": "누적 수익", "value": "67,200", "unit": "원", "icon_class": "fas fa-hand-holding-usd" },
]

# table_data = [
# 		{ "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 8시", "발전량": "301kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "하하" },
#         { "시간": "2022년 11월 2일 6시", "발전량": "302kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 13일 6시", "발전량": "310kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "450kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "365kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "323kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "123kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "310kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "604kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "343kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "245kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "335kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "245kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "446kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "356kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "1kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "1000kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
#         { "시간": "2022년 10월 1일 6시", "발전량": "300kw", "발전량 상태": "부족", "모듈온도": "20℃", "모듈 온도 상태": "낮음" },
# 	]

# class report(LoginRequiredMixin, TemplateView):
#     login_url = settings.LOGIN_URL
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['status_box'] = status
#         context['table_datas'] = json.dumps(table_data)
#         return context

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

class report(LoginRequiredMixin, TemplateView):
    login_url = settings.LOGIN_URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        queryset = ModuleData2.objects.values('dt', 'dt_hour', 'dc_kw1', 'dc_kw2', 'dc_kw3')
        # queryset_float = float(queryset.values)

        context['datas'] = json.dumps(list(queryset), cls=DecimalEncoder)
        return context