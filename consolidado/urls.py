from django.urls import include,path
from rest_framework import routers, urlpatterns
from . import views

router=routers.DefaultRouter()
router.register(r'consolidado',views.ConsolidadoViewSet,basename='consolidado')

urlpatterns=[path('',include(router.urls)),]