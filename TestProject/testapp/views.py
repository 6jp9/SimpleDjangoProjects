from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request,'testapp/home.html')
@login_required
def javatest(request):
    level = request.GET.get('level')
    if level:
        return redirect(f'/java_exam/?level={level}')
    return render(request,'testapp/javatest.html')
@login_required
def pythontest(request):
    level = request.GET.get('level')
    if level:
        return redirect(f'/py_exam/?level={level}')
    return render(request,'testapp/pythontest.html')
@login_required
def aptitudetest(request):
    level = request.GET.get('level')
    if level:
        return redirect(f'/apt_exam/?level={level}')
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

from testapp.models import Py_Question

def py_exam(request):
    level = request.GET.get('level')
    py_question = Py_Question.objects.filter(level=level,type='python')
    return render(request,'testapp/exam.html',{'question':py_question,'type':'Python','level':level})
def java_exam(request):
    level = request.GET.get('level')
    py_question = Py_Question.objects.filter(level=level,type='java')
    return render(request,'testapp/exam.html',{'question':py_question,'type':'Java','level':level})
def aptitude_exam(request):
    level = request.GET.get('level')
    py_question = Py_Question.objects.filter(level=level,type='frontend')
    return render(request,'testapp/exam.html',{'question':py_question,'type':'Front-End Tech','level':level})
    

