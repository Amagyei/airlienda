from django.db import models

# Create your models here.
class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email =models.EmailField(max_length=120)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField(default=3.0)
    profile_pic = models.ImageField(upload_to= 'static/images/', blank=True, null=True)

    def __str__(self):
        return f"student: {self.first_name} {self.last_name}"

