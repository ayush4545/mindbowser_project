from django.db import models

# Create your models here.

class manager(models.Model):
    email=models.EmailField(max_length=50)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    address=models.CharField(max_length=255)
    dob=models.DateField()
    company=models.CharField(max_length=255)
  
    class Meta:
        db_table='manager'
    
class employee(models.Model):
    id_no=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    address=models.CharField(max_length=255)
    dob=models.DateField()
    company=models.CharField(max_length=255)
    mobile=models.CharField(max_length=13)
    city=models.CharField(max_length=100)
    
    class Meta:
        db_table='employee'
    