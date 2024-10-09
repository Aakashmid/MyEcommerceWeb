from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def home(request):
    Data=Blog.objects.all()

    return render(request,'blog/index.html',{'blogs':Data})
def blogpost(request,id):
    length=len(Blog.objects.all())
    print(length)
    blog=Blog.objects.filter(post_id=id)
    
    if ( id >1 and id<length):
        nextBlog=Blog.objects.filter(post_id=id+1) # selecting next blog data by increaing value of post_id
        prevBlog=Blog.objects.filter(post_id=id-1) # selecting previous blog data by decreaing value of post_id
        return render(request,'blog/blogpost.html',{'blog':blog[0],'nextBlog':nextBlog[0],'prevBlog':prevBlog[0],'len':length})
    
    if id>1:
        prevBlog=Blog.objects.filter(post_id=id-1) # selecting previous blog data by decreaing value of post_id
        return render(request,'blog/blogpost.html',{'blog':blog[0],'prevBlog':prevBlog[0],'len':length})
    
    if id<length:
        nextBlog=Blog.objects.filter(post_id=id+1) # selecting next blog data by increaing value of post_id
        return render(request,'blog/blogpost.html',{'blog':blog[0],'nextBlog':nextBlog[0],'len':length})
    

    
    # blogs=Blog.objects.all()

    
