from django.urls import path, include

from rest_framework import routers

from profile_api import views


router = routers.DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hellow-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
