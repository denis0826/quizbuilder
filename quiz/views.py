from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Quiz


def index(request):
    queryset = Quiz.objects.all()

    context = {
        'objects_quiz': queryset,
        'title': "Quiz Builder",
    }
    return render(request, 'index.html', context)


def my_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return None

    else:
        return render(request, 'login.html', {})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def my_logout(request):
    try:
        logout(request)
    except KeyError:
        pass
    return redirect('login')


def quiz(request, quiz_id):
    quizname = get_object_or_404(Quiz, pk=quiz_id)
    context = {
        'quiz': quizname,
        'title': "Quiz"
    }
    return render(request, 'quiz.html', context)
