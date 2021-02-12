from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Profile
from .forms import ProfileForm, CheckPasswordForm, LoginForm
# decorators import
from django.contrib.auth.decorators import login_required
# needed when define signup:
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate
# needed when define user_delete:
from django.contrib.auth import logout as auth_logout
# needed when define profile_edit:
from django.core.files.storage import FileSystemStorage
from blog.models import Post 

# 이름 수정 필요.
def base(request):
    posts = Post.objects.all()
    new_post = []

    for post in posts:
        a=[post,post.count_likes_user()]
        new_post.append(a)
    
    sorted_post=sorted(new_post, key=lambda x: x[1], reverse=True)
    final_post=[]
    if len(sorted_post) <= 5:
        for i in range(len(sorted_post)):
            a=sorted_post[i][0]
            final_post.append(a)
    else:
        for i in range(5):
            a=sorted_post[i][0]
            final_post.append(a)

        
    ctx={'posts':final_post}
    
    return render(request, 'accounts/base.html',ctx)                                   

def login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user:
                auth_login(request, user)
                return redirect('accounts:profile')
            else:
                form.add_error(None, '아이디 또는 비밀번호가 유효하지 않습니다.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form})


def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                form.add_error(None, '비밀번호가 일치하지 않습니다.')
            else:
                user = form.save()
                # auth_login 인자로 user를 넘겨줘서 자동 로그인
                auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            next_url = reverse("accounts:profile") #회원가입 후 이동
            return redirect(next_url)
        else:
            return render(request, "accounts/signup.html", {'form':form})
    else:
        form=UserCreationForm()
        return render(request, "accounts/signup.html", {'form':form})

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    ctx = {'profile':profile}
    return render(request, 'accounts/profile.html', ctx)

@login_required
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=='POST':
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        if profileform.is_valid():
            profile = profileform.save()
            url = reverse("accounts:profile")
            return redirect(url)
    else:
        profileform = ProfileForm(instance=profile)
        return render(request, 'accounts/profile_edit.html', {'profileform':profileform, 'profile':profile})

# 계정 탈퇴(redirect url 추후 수정 필요)
@login_required
def user_delete(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)
        
        if password_form.is_valid():
            request.user.delete()
            auth_logout(request)
            url = reverse("accounts:base")
            return redirect(url)
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'accounts/user_delete.html', {'password_form':password_form})
