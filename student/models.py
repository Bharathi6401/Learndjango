from django.db import models

class Student(models.Model):
    first_name=models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob=models.DateField()
    enrollment_date=models.DateField(auto_now_add=True)

