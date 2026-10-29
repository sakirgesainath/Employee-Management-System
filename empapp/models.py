from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=50)
    Salary=models.FloatField(max_length=50)
    designation=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    age=models.IntegerField()
    dob=models.DateField()
    def __str__(self):
        return self.name