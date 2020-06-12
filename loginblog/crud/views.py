from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogPost
from .models import Post
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')

def gallery(request):
    posts = Post.objects
    post_list=Post.objects.all()
    paginator = Paginator(post_list, 5) # 페이지 나누기 (객체 3개씩)
    page = request.GET.get('page') # 요청한 페이지 값
    pages = paginator.get_page(page) # 해당 페이지 가져오기
    return render(request, 'gallery.html', {'posts':posts, 'pages':pages})

def detail(request, blog_id):
    details = get_object_or_404(Post, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def create(request):
    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=True)
            return redirect('gallery')
        return render(request, 'new.html', {'form':form})
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})

def update (request, pk):
    blog = get_object_or_404(Post, pk = pk)
    form = BlogPost(request.POST,request.FILES, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('gallery')
    return render(request, 'new.html', {'form':form})

def delete (request, pk):
    blog = get_object_or_404(Post, pk = pk)
    blog.delete()
    return redirect('gallery')