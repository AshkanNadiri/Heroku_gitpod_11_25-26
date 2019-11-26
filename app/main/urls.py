from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from drf import views as drf_views


router = routers.DefaultRouter()
router.register(r'users',drf_views.UserViewSet)
router.register(r'group',drf_views.GroupViewSet)
router.register(r'branch',drf_views.BranchViewSet)
router.register(r'customer',drf_views.CustomerViewSet)
router.register(r'account',drf_views.AccountViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls) ),
    path('api-auth/',include('rest_framework.urls', namespace = 'rest_framework')),
]
