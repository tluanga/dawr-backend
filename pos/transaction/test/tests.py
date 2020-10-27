import json
from django.http import response

from django.urls import reverse
from pos.transaction.models import PurchaseOrder, PurchaseOrderItem
from pos.transaction.serializers import (PurchaseOrderItemSerializer,
                                         PurchaseOrderSerializer)
from rest_framework import status
from rest_framework.test import APITestCase


class PurchaseOrderTestCase(APITestCase):
    def test_post(self):
        data={'ref_no':"ABC",'purchase_order_items': [
            {'product':1}]}
        response=self.client.post('/purchaseorder/',data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATE)
