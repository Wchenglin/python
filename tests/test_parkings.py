from django.test import TestCase,Client
from parking.models import Parking


class CommentsTestView(TestCase):

    def setUp(self):
        super(CommentsTestView,self).setUp()
        #data
        Parking.objects.create(parking_name='comment1')
        Parking.objects.create(parking_name='comment2')
        Parking.objects.create(parking_name='comment3')
        Parking.objects.create(parking_name='comment4')
        Parking.objects.create(parking_name='comment5')
        self.client = Client(enforce_csrf_checks=True)

    def test_CommentsView_get_noparm(self):
        response = self.client.get('/parkings')
        print(response.content)
        print(response.status_code)
        self.assertEqual(response.status_code,200)