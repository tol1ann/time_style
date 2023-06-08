from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'outfits', views.OutfitViewSet)
router.register(r'things', views.ThingViewSet)

urlpatterns = [
    path('', include(router.urls)),

] + router.urls