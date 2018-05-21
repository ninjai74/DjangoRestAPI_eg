from django.urls import path, include
from . import views
from rest_framework import routers

# default router
router = routers.DefaultRouter()
# to register the urls
router.register('languages', views.LanguageView)

urlpatterns = [
    path('', include(router.urls))
]
