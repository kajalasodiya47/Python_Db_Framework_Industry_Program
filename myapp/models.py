from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=15)
    role =  models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email + " | "+self.role
    
class Chairman(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    contact = models.CharField(max_length=20)
    blockno = models.CharField(max_length=10)
    houseno = models.CharField(max_length=10)
    pic = models.ImageField(upload_to="media/upload",default="default.png")

    def __str__(self):
        return self.firstname
    
class Member(models.Model): 
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    contact = models.CharField(max_length=20)
    blockno = models.CharField(max_length=10)
    houseno = models.CharField(max_length=10)   
    occupation = models.CharField(max_length=15)
    job_address = models.TextField()
    blood_grp = models.CharField(max_length=5)
    vehicle_details = models.CharField(max_length=15)
    pic = models.ImageField(upload_to="media/upload",default="default.png")