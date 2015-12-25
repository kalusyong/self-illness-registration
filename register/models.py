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
    workTime = models.CharField(max_length = 7)
    appointedPerson = models.CharField(max_length = 7,blank = True)
    appointNum = models.IntegerField(blank = True,null = True)
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

class Administrator(models.Model):
    userName = models.CharField(max_length = 50)
    Password = models.CharField(max_length = 30)
    userCategory = models.CharField(max_length = 5)

class Illness(models.Model):
    doctor = models.ManyToManyField(Doctor)
    division = models.ForeignKey(Division)
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 1000,blank = True)
    
class News(models.Model):
    Title = models.CharField(max_length = 100)
    Text = models.TextField(max_length = 1000)
    Image = models.ImageField(upload_to='./image/', blank=True,null=True)
    author = models.CharField(max_length = 20)
    Data = models.DateField()

class appointTable(models.Model):
    patient = models.ForeignKey(Patient, related_name='patient_set')
    doctorList = models.ManyToManyField(Doctor)
    weekNumber = models.CharField(max_length = 5)
    appintDate = models.DateField(blank=True,null=True)
    
    class Meta:
        ordering = ['appintDate'] 
    
    
    
    
    
    
    
    
    
    