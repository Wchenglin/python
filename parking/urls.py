from django.conf.urls import url
from parking.views import ParkingsView,ParkingView


urlpatterns = [
    url(r'^parkings$',ParkingsView.as_view()),
    url(r'^parkings/(?P<parking_id>.*)$',ParkingView.as_view())
]