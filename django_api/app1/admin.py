from django.contrib import admin
from .models import Obj, Branch

class ObjAdmin(admin.ModelAdmin):
    list_display=('pk','name','obj_code')

class BranchAdmin(admin.ModelAdmin):
    list_display=('pk','obj_name','branch_name','branch_code')

admin.site.register(Obj, ObjAdmin)
admin.site.register(Branch, BranchAdmin)
