from rest_framework import routers
from .views import ObjViewSet, BranchViewSet

router = routers.DefaultRouter()
router.register(r'obj', ObjViewSet)
router.register(r'branches', BranchViewSet)