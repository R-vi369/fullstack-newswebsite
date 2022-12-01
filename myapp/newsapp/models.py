from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
   
    # An AutoField is an IntegerField that automatically increments according to available IDs
    sno = models.AutoField(primary_key=True)
    # CharField is generally used for storing small strings like first name, last name, etc. To store larger text TextField is used.
    name = models.CharField(max_length=255,default='')
    phone = models.CharField(max_length=154,default='')
    email = models.CharField(max_length=74,default='')
    text = models.TextField()
    # timeStamp = models.DateTimeField(default=timezone.now)

# class Userdetail(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)

    
    def __str__(self):
        return 'data received from '+ self.name 