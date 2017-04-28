from django.conf.urls import url, include
from rest_framework import routers
from bangazon_api import views

from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'paymenttypes', views.PaymentTypeViewSet)
router.register(r'producttypes', views.ProductTypeViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'computers', views.ComputerViewSet)
router.register(r'training', views.TrainingViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'issues', views.CustomerIssueViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
