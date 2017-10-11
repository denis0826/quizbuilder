from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse

from .models import Quiz, Question, Choice, Answer, QuizSession


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
            return redirect('login')

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


def quiz(request, pk):

    quiz = Question.objects.filter(quiz=pk)
    quiz_title = Quiz.objects.get(id=pk)

    if request.user.is_authenticated():
        quiz_session = get_object_or_404(Quiz, id=pk)
        user = request.user
        session_save = QuizSession.objects.create(quiz=quiz_session, user=user.id, exam_date=timezone.now().date(), score=1)
        correct = 0
        wrong = 0
        answers = {}
        session_save.save()

        return HttpResponse(session_save.id, status=200)

    context = {
        'quiz': quiz,
        'title': quiz_title,
    }

    return render(request, 'quiz.html', context)


def question(request, pk):

    questions = Choice.objects.filter(question_id=pk)
    question_title = Question.objects.get(id=pk)
    session = QuizSession.objects.get(quiz=question_title.quiz)

    if request.method == "POST":
        choice = request.POST['choice']

        obj, created = Answer.objects.get_or_create(chosen_answer=choice, question_id=question_title.pk, session_id=session)
        obj.save()

        return HttpResponseRedirect('/')

    context = {
        'questions': questions,
        'title': question_title,
    }

    return render(request, 'question.html', context)


def results(request, sessionid):
    session = get_object_or_404(QuizSession, id=sessionid)
    return render(request, 'results.html', {'session': session})

