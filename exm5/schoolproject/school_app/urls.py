# school_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, ClassroomViewSet, TeacherViewSet, StudentViewSet

router = DefaultRouter()
router.register(r'schools', SchoolViewSet, basename='school')
router.register(r'classrooms', ClassroomViewSet, basename='classroom')
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]
