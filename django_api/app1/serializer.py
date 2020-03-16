from rest_framework import serializers

from .models import Obj, Branch

class ObjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obj
        fields = ('name','obj_code')

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('obj_name','branch_name','branch_code')