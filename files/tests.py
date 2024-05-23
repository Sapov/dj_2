from django.test import TestCase

# Create your tests here.

from .models import StatusProduct


class StatusProductTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        StatusProduct.objects.create(status='Оформлен')

    def test_status_label(self):
        status = StatusProduct.objects.get(id=1)
        field_label = status._meta.get_field('status').verbose_name
        self.assertEquals(field_label, 'Статус файла')

    def test_status_length(self):
        status = StatusProduct.objects.get(id=1)
        max_length = status._meta.get_field('status').max_length
        self.assertEquals(max_length, 64)
