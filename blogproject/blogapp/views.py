from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone # 타임존

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request): # new.html 띄우기
    return render(request, 'new.html')

def create(request): # DB에 넣기
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now() # 작성시점
    blog.save() # 객체를 DB에 저장  .delete (지우기)
    return redirect('/blog/'+str(blog.id)) # id는 int형이므로 형변환
    # redirect vs render