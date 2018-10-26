from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from company.models import Company
from company.form import CompanyForm
import json
from company.form import CompanyForm,CompanyPVForm
from parking.models import Parking

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class CompaniesView(View):


    #增加公司
    def post(self,request):
        res = CompanyForm(request.POST)
        if not res.is_valid():
            return HttpResponse(status=422)
        Company.objects.create(company_name=res.data.get('company_name'))
        return HttpResponse(status=201)

    #获取公司信息
    def get(self,request):
        res = CompanyForm(request.GET)
        if not res.is_valid():
            return HttpResponse(status=422)
        company = Company.objects.filter(company_name=res.data.get('company_name'))
        print(company.values())
        return HttpResponse(status=200)

class CompanyView(View):

    #修改公司信息（例：公司名字）
    def put(self,request,company_id):
        stream = request.body.decode()
        json_data = json.loads(stream)
        Company.objects.filter(company_id=company_id).update(company_name=json_data['company_name'])
        return HttpResponse(status=202)

    #删除公司信息
    def delete(self,request,company_id):
       Company.objects.filter(company_id=company_id).delete()
       return HttpResponse(status=204)

@method_decorator(csrf_exempt,name='dispatch')
class CompanyParkingsView(View):

    #通过公司查询某一个停车场信息
    def get(self,request,company_id):
        res = CompanyPVForm(request.GET)
        if not res.is_valid():
            return HttpResponse(status=422)
        company = Company.objects.get(company_id=company_id)
        print(type(company))
        parks = company.parking_company
        parks = parks.values()
        park = parks.get(parking_id=res.data.get('parking_id'))
        print('停车场名称：'+park['parking_name'])
        return HttpResponse(status=200)









