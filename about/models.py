from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile/')
    resume = models.FileField(upload_to='resume/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
