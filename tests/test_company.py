from django.test import TestCase,Client
from company.models import Company


class CommentsTestView(TestCase):

    def setUp(self):
        super(CommentsTestView,self).setUp()
        #data
        Company.objects.create(company_name='comment1')
        Company.objects.create(company_name='comment2')
        Company.objects.create(company_name='comment3')
        Company.objects.create(company_name='comment4')
        Company.objects.create(company_name='comment5')
        self.client = Client(enforce_csrf_checks=True)

    def test_CommentsView_get_noparm(self):
        response = self.client.get('/companies')
        print(response.content)
        print(response.status_code)
        self.assertEqual(response.status_code,200)

