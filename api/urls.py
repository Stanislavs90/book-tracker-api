from django.urls import path, include
from . import views
from rest_framework import routers
from .views import BookViewSet, AuthorViewSet, CharacterViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)
router.register('Characters', CharacterViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
    
]
