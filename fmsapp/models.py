from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Dam (models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    no_fishes = models.CharField(blank=True, max_length=100)
    fish_categories = models.CharField (blank=True, max_length=100)
    location = models.TextField(blank=True, max_length=700)
    about = models.TextField(blank=True, max_length=2000)

    def __str__(self):
        return self.name;
    

class Department (models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=700, default='Description goes here')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("fms:dept_single", kwargs={"pk": self.pk})
    

class Staff (models.Model):
    STATES = (('edo','Edo'),('ekiti','Ekiti'),('kogi','Kogi'),('kwara','Kwara'),('lagos','Lagos'),
        ('ogun','Ogun'),('ondo','Ondo'),('osun','Osun'),('oyo','Oyo'),)
    image = models.ImageField(blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    stipend = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=11)
    state = models.CharField(max_length=20, choices=STATES, default='edo')
    country = models.CharField(max_length=20, default='Nigeria')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    work_description = models.TextField(max_length=1000)

    def __str__(self):
        return self.first_name+'-'+self.last_name

    def get_absolute_url(self):
        return reverse("fms:staff_single", kwargs={"pk": self.pk})
    
    

class User (AbstractUser):
    image = models.ImageField(blank=True)


class Fish(models.Model):
    name = models.CharField(max_length=50)
    types = models.CharField(max_length=50)
    total = models.IntegerField()
    immersiveDate = models.DateField(auto_now_add=True, null=True)
    HarvestDate = models.CharField(max_length=18, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class TimeLine(models.Model):
    number = models.IntegerField()
    dam = models.CharField(max_length=2)
    others = models.TextField(max_length=9000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Sales (models.Model):
    types = models.CharField(max_length=12)
    weight = models.IntegerField()
    amount = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.types

class Debtors (models.Model):
    name = models.CharField(max_length=90)
    file_no = models.CharField(max_length=50)
    quantity = models.IntegerField()
    department = models.CharField(max_length=50)
    amount = models.IntegerField()
    signature = models.ImageField()
    created = models.DateField(auto_now_add=True, null=True)