from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name

class Classroom(models.Model):
    grade = models.PositiveIntegerField()
    section = models.CharField(max_length=10)
    school = models.ForeignKey(School, related_name='classrooms', on_delete=models.CASCADE)

    def __str__(self):
        return f"Grade {self.grade} - Section {self.section}"

class Teacher(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    schools = models.ManyToManyField(School, related_name='teachers', blank=True)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    classroom = models.ForeignKey(Classroom, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
