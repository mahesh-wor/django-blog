from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
#creating profile pic + 1to1 relation shipp

class Profile(models.Model): #inherit models.Models
    user =  models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):      #if users.Profile class called it returns below
        return f'{self.user.username} Profile'

#for resizing prifile pic

    def save(self, force_insert=False, force_update=False, using=None):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



