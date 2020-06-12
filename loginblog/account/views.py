from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']: # 비밀번호 확인절차
            user = User.objects.create_user( username=request.POST['username'], password=request.POST['password1']) # id와 pw를 받아서 넘기기 
            auth.login(request, user) # 회원가입 후 자동로그인
            return redirect('home') # 리다이렉트
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password) # 유효한 ID/PW인지 확인
        if user is not None: # None이 아니라면 -> 회원이 맞다면
            auth.login(request, user)
            return redirect('home') # home으로 리다이렉트
        else: # 로그인 실패 시
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else: # 그 이와의 오류
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request) # 로그아웃 함수 사용
        redirect('home') # 리다이렉트
    return render(request, 'login.html') # 그냥 다 실패 시
