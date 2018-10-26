from django.conf.urls import url
from company.views import CompaniesView,CompanyView,CompanyParkingsView


urlpatterns = [
    url(r'^companies$',CompaniesView.as_view()),
    url(r'^companies/(?P<company_id>.*)/parkings$', CompanyParkingsView.as_view()),
    url(r'^companies/(?P<company_id>.*)$',CompanyView.as_view()),

]