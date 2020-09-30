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

######################---Category---######
from pos.category.views import CategoryViewSet
router.register('category',CategoryViewSet)

######################---Category---######
from pos.category.views import CategoryViewSet
router.register('category',CategoryViewSet)

######################--Unit Of Measurement---######
from pos.unit_of_measurement.views import UnitOfMeasurementViewSet
router.register('unit_of_meaurement',UnitOfMeasurementViewSet)


#######################3---product----###########
from pos.product.views import (
                               ProductViewSet,
                               ProductCostPriceViewSet,
                               ProductSellPriceViewSet)

router.register('product',ProductViewSet)
router.register('productcostprice',ProductCostPriceViewSet)
router.register('productsellprice',ProductSellPriceViewSet)

######################--Inventory---############333
from pos.inventory.views import (ProductPurchaseViewSet,                                  
                                  ProductStockViewSet,
                                 )


router.register('productpurchase',ProductPurchaseViewSet)
router.register('productstock',ProductStockViewSet)

####################---Sell--------##############
from pos.sell.views import (OrderItemViewSet, OrderViewSet)
router.register('orderitem',OrderItemViewSet)
router.register('order',OrderViewSet)




urlpatterns=router.urls