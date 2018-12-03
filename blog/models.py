from django.db import models
from django.utils import timezone #for time
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import admin

# Create your models here.
class Tag(models.Model):
    tag_name=models.CharField(primary_key=True,max_length=20)
    

    def __str__(self):
        return self.tag_name


class Post(models.Model):  #fields here

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_tag=models.ManyToManyField(Tag)
    #tags_content = models.CharField(max_length=2,choices=TAGS,default='django-blog')

    def __str__(self):
        return self.title

###for redirecting while new blog is created
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

#class Person(models.Model):
#   name =models.CharField(max_length=120)
#
#    def __str__(self):
#       return self.name

#class Group(models.Model):
#    name =models.CharField(max_length=120)
#    members = models.ManyToManyField(Person,through="Membership")
#
#    def __str__(self):
#        return self.name

#class Membership(models.Model):
#    person=models.ForeignKey(Person,on_delete=models.CASCADE)
#    group= models.ForeignKey(Group,on_delete=models.CASCADE)
#    #date_joined=models.DateField()
#    invite_reason=models.CharField(max_length=120)
