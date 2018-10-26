from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from parking.models import Parking
from parking.form import ParkingForm
from company.models import Company
import json

@method_decorator(csrf_exempt,name='dispatch')
class ParkingsView(View):

    #添加停车场
    def post(self,request):
        stream = request.body.decode()
        json_data = json.loads(stream)
        Parking.objects.create(parking_name=json_data['parking_name'])
        return HttpResponse(status=200)

class ParkingView(View):

    #为停车场添加外键
    def put(self,request,parking_id):
        stream = request.body.decode()
        json_data = json.loads(stream)
        Parking.objects.filter(parking_id=parking_id).update(company_id=json_data['company_id'])
        return HttpResponse(status=200)

    #获取停车场所关联公司属性(例：公司名字)
    def get(self,request,parking_id):
        res = ParkingForm(request.GET)
        if not res.is_valid():
            return HttpResponse(status=422)
        parking = Parking.objects.get(parking_id=parking_id)
        company = Company.objects.get(company_id=parking.company_id)
        print('公司名称：'+company.company_name)
        return HttpResponse(status=200)


