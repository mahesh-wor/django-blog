from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    ##for dynamic urls
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('about/',views.about, name='blog-about'),

]


##for create
#post_form.html

#post_confirm_delete.html
#<app>/<model>_<viewtype>.html
