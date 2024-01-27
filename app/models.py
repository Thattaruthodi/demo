from django.db import models

# Create your models here.
class student_details(models.Model):
 
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    contact = models.IntegerField(null=True)

