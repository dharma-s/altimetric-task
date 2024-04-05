# telecom_mobility_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from customers.views import PlanViewSet, CustomerViewSet
from accounts.views import register_user
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'plans', PlanViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
    path('api/register/', register_user, name='register_user'),
]
