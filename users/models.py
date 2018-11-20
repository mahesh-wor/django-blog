from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#creating profile pic + 1to1 relation shipp

class Profile(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'
