from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    phone_no = models.CharField(max_length=16)
    gender = models.CharField(max_length=8, choices=(
        ('male','male'),
        ('female', 'female'),
        ('other','other')
    ))
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.email