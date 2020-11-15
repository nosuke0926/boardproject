from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def signupfunc(request):
    user2 = User.objects.get(username='user')
    print(user2.email)
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            # getメソッドは値が取得できないとエラーを返す
            User.objects.get(username=username2)
            return render(request, 'signup.html',{'error':'登録済です'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return render(request,'signup.html',{'some':100})

    return render(request, 'signup.html', {'some': 100})

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('signup')
        else:
            return redirect('login')

    return render(request, 'login.html')
