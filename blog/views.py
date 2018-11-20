from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.views.generic import (
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,

)
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

"""
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
"""
##non convention

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'    #blog/post_detail
    ordering = ['-date_posted']

##DetailView
class PostDetailView(DetailView):
    model = Post

#give fields for the form
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields =['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
##UpdateView

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields =['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url ='/'  #for redirecting after success deleting.
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False





def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
