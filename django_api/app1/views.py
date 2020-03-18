import django_filters
from rest_framework import viewsets, filters
from .models import Obj, Branch
from .serializer import ObjSerializer, BranchSerializer

class ObjViewSet(viewsets.ModelViewSet):
    queryset = Obj.objects.all()
    serializer_class = ObjSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
