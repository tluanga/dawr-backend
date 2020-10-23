from rest_framework import routers
#####################################
router=routers.DefaultRouter()


#######################TAX####################
from pos.tax.views import GSTCodeViewSet
router.register('gstcode',GSTCodeViewSet)
####################################

#####################---WAREHOUSE---#############
from pos.warehouse.views import WareHouseViewSet
router.register('warehouse',WareHouseViewSet)

######################---SUPPLIER---###########333
from pos.supplier.views import SupplierViewSet
router.register('supplier',SupplierViewSet)

######################---Customer---######
from pos.customer.views import CustomerTypeViewSet, CustomerViewSet
router.register('customertype',CustomerTypeViewSet)
router.register('customer',CustomerViewSet)



#######################3---product----###########
from pos.product.views import (UnitOfMeasurementViewSet,
                               CategoryViewSet,
                               ProductViewSet,
                               ProductCostPriceViewSet,
                               ProductSalePriceViewSet)
router.register('unitofmeasurement',UnitOfMeasurementViewSet)
router.register('category',CategoryViewSet)
router.register('product',ProductViewSet)
router.register('productcostprice',ProductCostPriceViewSet)
router.register('productsaleprice',ProductSalePriceViewSet)

######################--Inventory---############333
from pos.inventory.views import (ProductPurchaseViewSet,                                  
                                    ProductStockViewSet,
                                    SellItemViewSet,
                                    SellViewSet
                                 )


router.register('productpurchase',ProductPurchaseViewSet)
router.register('productstock', ProductStockViewSet)
router.register('Sellitem', SellItemViewSet)
router.register('Sell',SellViewSet)

####################---Sell--------##############
from pos.sell.views import (OrderItemViewSet, OrderViewSet)
router.register('orderitem',OrderItemViewSet)
router.register('order',OrderViewSet)

from django.urls import path, include

urlpatterns = [
    path('', include(router.urls)),
    path('', include('pos.product.urls'))
]