from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from drf.serializer import UserSerializer, GroupSerializer, BranchSerializer, CustomerSerializer, AccountSerializer
from drf.models import Branch, Customer, Account

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint will let you edit users or viewed them.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint will let you edit or viewed them.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

