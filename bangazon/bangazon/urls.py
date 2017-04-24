from django.conf.urls import url, include
from rest_framework import routers
from bangazon_api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'payment-type', views.PaymentTypeViewSet)
router.register(r'product-type', views.ProductTypeViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'department', views.DepartmentViewSet)
router.register(r'computer', views.ComputerViewSet)
router.register(r'training', views.TrainingViewSet)
router.register(r'training-session', views.TrainingSessionViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'order-product', views.OrderProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
