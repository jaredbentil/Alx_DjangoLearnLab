from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api import views

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
