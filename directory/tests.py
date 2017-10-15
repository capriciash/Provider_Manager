from django.test import TestCase
from django.utils import timezone #for model test
from django.core.urlresolvers import reverse #for view test
# Test a model
from .models import Provider, Driver

class ProviderModelTests(TestCase):
    def test_provider_creation(self):
        provider = Provider.objects.create(
            business_name="ABC Provider",
            address="123 Main St, Portland, OR 97222",
            business_license="208KSHD",
            phone_number="5555555555"
        )
        now = timezone.now()
        self.assertLess(provider.created_at, now)
        # self.assertIn()

class DriverModelTests(TestCase):
    def setUp(self):
        self.provider = Provider.objects.create(
            business_name="ABC Provider",
            address="123 Main St, Portland, OR 97222",
            business_license="208KSHD",
            phone_number="5555555555"
        )
    def test_driver_creation(self):
        driver = Driver.objects.create(
            first_name="First",
            last_name="Last",
            driver_id="927495",
            birth_date="1982-01-01",
            hire_date="2017-01-10",
            provider=self.provider
        )

#View test
class ProviderViewsTests(TestCase):
    def setUp(self):
        self.provider = Provider.objects.create(
            business_name="ABC Provider",
            address="123 Main St, Portland, OR 97222",
            business_license="208KSHD",
            phone_number="5555555555"
        )
        self.provider2 = Provider.objects.create(
            business_name="DEF Provider",
            address="456 Main St, Portland, OR 97222",
            business_license="374KBDH",
            phone_number="7777777777"
        )
        self.driver = Driver.objects.create(
            first_name="First",
            last_name="Last",
            driver_id="927495",
            birth_date="1982-01-01",
            hire_date="2017-01-10",
            provider=self.provider
        )
    def test_provider_list_view(self):
        resp = self.client.get(reverse('directory:provider_list')) #responses,
        # reverse covers url testing too bc it requires a working url for the test
        self.assertEqual(resp.status_code,200)
        self.assertIn(self.provider, resp.context['providers']) #the name of the views context
        self.assertIn(self.provider2, resp.context['providers'])
        self.assertTemplateUsed(resp, 'directory/provider_list.html') #test template used
        self.assertContains(resp, self.provider.business_name) #template contains first provider

    def test_provider_detail_view(self):
        resp = self.client.get(reverse('directory:provider_detail',
                                    kwargs={'pk': self.provider2.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.provider2, resp.context['provider'])
        self.assertTemplateUsed(resp, 'directory/provider_detail.html') #test template used
        self.assertContains(resp, self.provider2.business_name) #template contains first provider

    def test_driver_detail_view(self):
        resp = self.client.get(reverse('directory:driver_detail', kwargs={
                                    'provider_pk': self.provider.pk,
                                    'driver_pk': self.driver.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.driver, resp.context['driver'])
        self.assertTemplateUsed(resp, 'directory/driver_detail.html') #test template used
        self.assertContains(resp, self.driver.first_name) #template contains first provider

    # tip for model creation
        # for x in range(1, 3):
        #     Article.objects.create(
        #         writer=self.writer,
        #         headline='Article {}'.format(x),
        #         content='Something about {}'.format(x),
        #         publish_date=datetime.datetime.today()
        #     )
