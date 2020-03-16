import django_filters
from rest_framework import viewsets, filters
from .models import Obj, Branch
from .serializer import ObjSerializer, BranchSerializer

class ObjViewSet(viewsets.ModelViewSet):
    query = Obj.objects.all()
    serializer_class = ObjSerializer

class BranchViewSet(viewsets.ModelViewSet):
    query = Branch.objects.all()
    serializer_class = BranchSerializer
