from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import View
from django.views import generic

from .models import Quiz, Question

def index(request):
    queryset = Quiz.objects.all()

    context = {
        'objects_quiz' : queryset,
        'title': "Quiz Builder"
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

# def quiz(request, quiz_id):
#     quiz = Quiz.objects.get(pk=quiz_id)

#     context = {
#         'quiz': quiz,
#         'title': "Quiz"
#     }
    
#     return render(request, 'quiz.html', context ) 

# def quiz_list(request, quiz_id):    
#     question = get_object_or_404(Quiz, pk=quiz_id)
#     return render(request, 'quiz.html', {'question': question})

class DetailView(generic.DetailView):
    model = Quiz
    template_name = 'quiz.html'


def choose(request, quiz_id):
    p = get_object_or_404(Quiz, pk=quiz_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question': p,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
