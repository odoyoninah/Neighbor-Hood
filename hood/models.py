from email.mime import image
from django.db import models

# Create your models here.
class Hood(models.Model):
    hood_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    occupants = models.IntegerField()
    police_station_address = models.EmailField(max_length=50)
    police_station_name = models.CharField(max_length=50)
    health_care_address = models.EmailField(max_length=50)
    health_care_name = models.CharField(max_length=50)
    posts = models.ImageField(upload_to='posts/')
    description = models.TextField()
    admin = models.ForeignKey('Admin', on_delete=models.CASCADE)

    def create_hood(self):
        self.save()
        
    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    def update_hood(self):
        self.save()

    def __str__(self):
        return self.name

class Business(models.Model):
    hood_id = models.ForeignKey(Hood, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    admin = models.ForeignKey('Admin', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    admin = models.ForeignKey('Admin', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    post = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    hood = models.ForeignKey('Hood', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.title





 
