from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse
# Create your views here.


#posts = [
#        {
#            'author':'invoron',
#            'content':'Dota 2 does seem to care whether you know how to play it or not.',
#            'date_posted':'August 27, 2018'
#        },
#        {
#            'author':'lynchmob',
#            'title':'dotatutorial_noob',
#        }
#]




def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
