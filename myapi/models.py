from django.db import models

# Create your models here.
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField(max_length=100)
    type=models.CharField(choices=(('it','IT'),('non it ','Non it'),('mobile phones','Mobile Phones')),max_length=15)
    added_date=models.DateField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=60)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=20,choices=(
        ('Manager','manager'),('Software','software'),('project lead','pl')
    ))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)