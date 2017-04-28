from rest_framework import viewsets
from bangazon_api.models import *
from bangazon_api.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    author: Meg Ducharme
    """
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        """
        Restrict the properties returned based on authentication.
        
        author: Gilberto Diaz
        :return: customer serializer
        """
        if self.request.user.is_superuser:
            return CustomerSerializer
        return CustomerRestrictedSerializer


class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    author: Meg Ducharme
    """
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    author: Meg Ducharme
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    author: Meg Ducharme
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    author: Meg Ducharme
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employee data to be viewed and edited.
    author: Gilberto Diaz
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows department data to be viewed and edited.
    author: Gilbert Diaz
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class ComputerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows computer data to be viewed and edited.
    author: Gilberto Diaz
    """
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class TrainingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows training data to be viewed and edited.
    author: Gilberto Diaz
    """
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class CustomerIssueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows training data to be viewed and edited.
    author: Gilberto Diaz
    """

    queryset = CustomerIssue.objects.all()
    serializer_class = CustomerIssueSerializer
