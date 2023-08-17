from django.test import TestCase

from neulhaerang.models import Neulhaerang


# Create your tests here.

class NeulhaerangListTest(TestCase):
    Neulhaerang.objects.filter(name='어린이').order_by('-updated_date')
    pass