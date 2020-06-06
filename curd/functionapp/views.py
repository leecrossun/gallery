from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogPost
from .models import Blog
from django.utils import timezone


def welcome (request):
    return render(request, 'viewcrud/index.html')

def read (request):
    blogs = Blog.objects.all()
    return render(request, 'viewcrud/funccrud.html', {'blogs':blogs})

def create(request):
    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES) # request.FILES를 해주어야 유저가 올린 미디어 파일도 제대로 넘어온다.
        if form.is_valid():
            post = form.save(commit=False) # SAVE만 해놓고 커밋을 미루는 것인데, 그냥 timezone을 미리 해줘도 되는 것 같다.
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
        return render(request, 'viewcrud/new.html', {'form':form})
    else:
        form = BlogPost()
        return render(request, 'viewcrud/new.html', {'form':form})

# 특정한 블로그글을 대상으로 실행 -> pk값 필요
def update (request, pk):
    # 어떤 블로그(객체)
    blog = get_object_or_404(Blog, pk = pk)

    # 블로그 객체 pk에 맞는 입력공간 가져오기
    form = BlogPost(request.POST,request.FILES, instance=blog) # 3번째 인자 주의

    if form.is_valid():
        form.save()
        return redirect('home')
        
    return render(request, 'viewcrud/new.html', {'form':form})

def delete (request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')