
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'author', AuthorViewSet)

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]
