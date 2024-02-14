from django.db import models

# Create your models here.
class Student(models.Model):
    firstName=models.CharField(max_length=50,null=False,blank=False)
    lastName=models.CharField(max_length=50,null=False,blank=False)
    birthdate=models.DateField()
    country=models.CharField(max_length=50,null=False,blank=False)
    university=models.CharField(max_length=50,null=False,blank=False)
    phone=models.CharField(max_length=50,null=False,blank=False)
    img=models.CharField(max_length=50,null=False,blank=False)
    email=models.EmailField()
    password=models.CharField(max_length=12,null=False,blank=False)

class Scholarship(models.Model): 
	specialization=models.TextField(default='')
	img=models.CharField(max_length=50,null=False,blank=False)
	type=models.BooleanField(default=True)
	num_of_disks=models.IntegerField()
	details=models.TextField()
	summary=models.TextField()
	stage=models.CharField(max_length=20,null=False,blank=False,
    choices=(
        ('1','Bachalor'),
        ('2','Master'),
        ('3','Doctoral'),
    )
    )
	rating=models.IntegerField()
	deadline=models.DateField()
	cost=models.FloatField()
    
class Country(models.Model):
	name=models.CharField(max_length=20)

class Country_Scholarship(models.Model):
	country=models.ForeignKey(Country,on_delete=models.CASCADE)
	scholarship=models.ForeignKey(Scholarship,on_delete=models.CASCADE)
	
class Order(models.Model):
    degree=models.CharField(max_length=50,null=False,blank=False)
    identification=models.CharField(max_length=50,null=False,blank=False)
    passport=models.CharField(max_length=50,null=False,blank=False)
    money_transaction_num=models.CharField(max_length=50,null=False,blank=False)
    scholarship=models.ForeignKey(Scholarship,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    state=models.IntegerField(default=2,
    choices=(
        (0,'Accepted'),
        (1,'Rejected'),
        (2,'Under_consideration'),
    ))

class University(models.Model):
   name=models.CharField(max_length=50,null=False,blank=False)
   logo=models.CharField(max_length=50,null=False,blank=False)
   url=models.URLField()
   country=models.ForeignKey(Country,on_delete=models.CASCADE)

class Comment(models.Model):
    email=models.CharField(max_length=50)
    fallName=models.CharField(max_length=50)
    msg=models.TextField()

class Rate(models.Model):
    scholarship=models.ForeignKey(Scholarship,on_delete=models.CASCADE)
    one=models.IntegerField()
    two=models.IntegerField()
    three=models.IntegerField()
    four=models.IntegerField()
    five=models.IntegerField()

class Std_Rate(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    scholarship=models.ForeignKey(Scholarship,on_delete=models.CASCADE)
    rate=models.IntegerField()

class University_Sch(models.Model):
    scholarship=models.ForeignKey(Scholarship,on_delete=models.CASCADE)
    university=models.ForeignKey(University,on_delete=models.CASCADE)