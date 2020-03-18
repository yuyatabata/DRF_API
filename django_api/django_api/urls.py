from django.contrib import admin
from django.urls import path, include
from app1.urls import router as obj_api_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(obj_api_router.urls)),
]
