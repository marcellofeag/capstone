from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from LittleLemonAPI.models import *
from LittleLemonAPI.serializers import *

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Ice Cream", price="80", inventory=100)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "Ice Cream : 80")
        
class MenuViewTest(TestCase):
    
    def setUp(self):
        self.item1 = MenuItem.objects.create(title="Burger", price="7", inventory=8)
        self.item2 = MenuItem.objects.create(title="Fries", price="3.5", inventory=2)
        self.item3 = MenuItem.objects.create(title="Drink", price="2.5", inventory=15)
        self.client = APIClient()
        
    def test_getall(self):
        response = self.client.get('/api/menu-items/')