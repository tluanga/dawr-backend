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
                               ProductSellPriceViewSet)
router.register('unitofmeasurement',UnitOfMeasurementViewSet)
router.register('category',CategoryViewSet)
router.register('product',ProductViewSet)
router.register('productcostprice',ProductCostPriceViewSet)
router.register('productsellprice',ProductSellPriceViewSet)

######################--Inventory---############333
from pos.transaction.views import (PurchaseOrderItemViewSet,                                  
                                    ProductStockViewSet,                                   
                                 )


router.register('productpurchase',PurchaseOrderItemViewSet)
router.register('productstock', ProductStockViewSet)


####################---Sell--------##############
from pos.sell.views import (OrderItemViewSet, OrderViewSet, ModeOfSellViewSet,SettleBillViewSet)
router.register('orderitem',OrderItemViewSet)
router.register('order',OrderViewSet)
router.register('modeofsell',ModeOfSellViewSet)
router.register('settlebill',SettleBillViewSet)


from django.urls import path, include

urlpatterns = [
    path('', include(router.urls)),
    path('', include('pos.product.urls'))
]