from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request,'testapp/home.html')
@login_required
def javatest(request):
    return render(request,'testapp/javatest.html')
@login_required
def pyhtontest(request):
    return render(request,'testapp/pythontest.html')
@login_required
def aptitudetest(request):
    return render(request,'testapp/aptitudetest.html')

def logout_view(request):
    return render(request,'registration/custom_logout.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.set_password(user.password) 
            user.save()
            return HttpResponseRedirect('/accounts/login')
    else:
        form = SignUpForm()
    return render(request, 'testapp/signup.html', {'form': form})

from testapp.models import Question

def exam(request):
    question = Question.objects.all()
    return render(request,'testapp/exam.html',{'question':question})

