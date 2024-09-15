# school_app/serializers.py

from rest_framework import serializers
from .models import School, Classroom, Teacher, Student

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address']

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'grade', 'section', 'school']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender', 'schools', 'classrooms']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender', 'classroom']

# สำหรับ Detail Views ที่ต้องการข้อมูลเพิ่มเติม

class SchoolDetailSerializer(serializers.ModelSerializer):
    classroom_count = serializers.IntegerField(read_only=True)
    teacher_count = serializers.IntegerField(read_only=True)
    student_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address', 'classroom_count', 'teacher_count', 'student_count']

class ClassroomDetailSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Classroom
        fields = ['id', 'grade', 'section', 'school', 'teachers', 'students']

class TeacherDetailSerializer(serializers.ModelSerializer):
    classrooms = ClassroomSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender', 'schools', 'classrooms']

class StudentDetailSerializer(serializers.ModelSerializer):
    classroom = ClassroomSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender', 'classroom']
