from django.shortcuts import render

from rest_framework import viewsets, filters
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .models import School, Classroom, Teacher, Student
from .serializers import (
    SchoolSerializer, SchoolDetailSerializer,
    ClassroomSerializer, ClassroomDetailSerializer,
    TeacherSerializer, TeacherDetailSerializer,
    StudentSerializer, StudentDetailSerializer
)

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SchoolDetailSerializer
        return SchoolSerializer

    def get_queryset(self):
        return School.objects.annotate(
            classroom_count=Count('classrooms', distinct=True),
            teacher_count=Count('teachers', distinct=True),
            student_count=Count('classrooms__students', distinct=True)
        )

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['school']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClassroomDetailSerializer
        return ClassroomSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['schools', 'classrooms', 'first_name', 'last_name', 'gender']
    search_fields = ['first_name', 'last_name']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TeacherDetailSerializer
        return TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['classroom__school', 'classroom', 'first_name', 'last_name', 'gender']
    search_fields = ['first_name', 'last_name']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentDetailSerializer
        return StudentSerializer
