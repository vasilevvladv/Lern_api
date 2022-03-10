from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import PostViewSet

router_v1 = routers.DefaultRouter()


router_v1.register(r'posts', PostViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
] 


