import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from .models import Customer, CustomerType
from .serializers import CustomerSerializer, CustomerTypeSerializer

class CustomerTypeTestCase(APITestCase):
    def test_customertype(self):
        data = {"name": "ordinary", "discount_percentage": "10",
                "remarks": "ordinary customers have 10 percent discount", "active": True}
    response = self.client.post("/customertype", data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CustomerTestCase(APITestCase):
    def test_customer(self):
        data = {
            "name": "John",
            "address": "10",
            "city": "Aizawl",
            "contact_no":"9862374562",
            "email": "John@gmail.com",
            "gst_no": "MBC11"
    }
    response = self.client.post("/customer", data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                