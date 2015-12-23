from django.db import models

# Create your models here.
class Division(models.Model):
    divisionID = models.CharField(max_length = 20)
    name = models.CharField(max_length = 20)
    def __unicode__(self):
        return self.name
class Doctor(models.Model):
    userName = models.CharField(max_length = 50)
    Password = models.CharField(max_length = 30)
    userCategory = models.CharField(max_length = 5)
    name = models.CharField(max_length = 20,blank = True)
    age = models.IntegerField(blank = True,null = True)
    sex = models.CharField(max_length = 5,blank = True)
    phoneNumber = models.CharField(max_length = 15,blank = True)
    intro = models.TextField(max_length = 200,blank = True)
    division = models.ForeignKey(Division)
    def __unicode__(self):
        return self.name
class Patient(models.Model):
    userName = models.CharField(max_length = 50)
    Password = models.CharField(max_length = 30)
    userCategory = models.CharField(max_length = 5)
    name = models.CharField(max_length = 20,blank = True)
    age = models.IntegerField(blank = True,null = True)
    sex = models.CharField(max_length = 5,blank = True)
    phoneNumber = models.CharField(max_length = 15,blank = True)
    doctorsList = models.ManyToManyField(Doctor)

class Administrator(models.Model):
    userName = models.CharField(max_length = 50)
    Password = models.CharField(max_length = 30)
    userCategory = models.CharField(max_length = 5)

class Illness(models.Model):
    doctor = models.ManyToManyField(Doctor)
    division = models.ForeignKey(Division)
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 1000)
    
    
class News(models.Model):
    Title = models.CharField(max_length = 100)
    Text = models.TextField(max_length = 1000)
    Image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True,null=True)
    author = models.CharField(max_length = 20)
    Data = models.DateField()
   