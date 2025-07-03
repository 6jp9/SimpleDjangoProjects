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

#####################################################################

from django.contrib.auth.models import User

def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        real_otp = request.session.get('otp')
        data = request.session.get('signup_data')

        if entered_otp == real_otp:
            # Create and save the user
            user = User(
                username=data['username'],
                email=data['email']
            )
            user.set_password(data['password'])  # Assuming you use password1 in your form
            user.save()
            # Clear session data
            del request.session['signup_data']
            del request.session['otp']

            return redirect('/accounts/login')
        else:
            return render(request, 'testapp/otpverify.html', {'error': 'Invalid OTP'})
    return render(request, 'testapp/otpverify.html')


from django.core.mail import send_mail
from random import randint

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Store user data in session temporarily
            request.session['signup_data'] = form.cleaned_data
            otp = str(randint(100000, 999999))
            request.session['otp'] = otp

            # Send OTP to email
            send_mail(
                subject='Quiz App Email Verification',
                message = f"Hello {form.cleaned_data['username']},\nYour OTP for verification is {otp}.",
                from_email='<your_email>.com',
                recipient_list=[form.cleaned_data['email']],
                fail_silently=False,
            )
            return redirect('verify_otp')
    else:
        form = SignUpForm()
    return render(request, 'testapp/signup.html', {'form': form})

#####################################################################

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False) 
#             user.set_password(user.password) 
#             user.save()
#             return HttpResponseRedirect('/accounts/login')
#     else:
#         form = SignUpForm()
#     return render(request, 'testapp/signup.html', {'form': form})

from testapp.models import Py_Question




def py_exam(request):
    level = request.GET.get('level')
    py_question = Py_Question.objects.filter(level=level,type='python')

    if request.method == 'POST':
        score = 0
        total = py_question.count()
        result = []

        for q in py_question:
            valid = False
            user_answer = request.POST.get(f'question_{q.id}')
            user_answer_text='Not Attempted'

            if user_answer == q.correct_answer:
                score+=1
                valid = True
            if user_answer!=None:
                user_answer_text = str(user_answer)+'. '+str(getattr(q,'option_'+user_answer.lower()))

            result.append({'question':q.question_text,
                           'user_answer':user_answer_text,
                           'right_answer':str(q.correct_answer)+'. '+str(getattr(q,'option_'+str(q.correct_answer).lower())),
                           'valid':valid,
                           })
        return render(request,'testapp/result.html',{'result':result,'score':score,'total':total,'type':'Python','level':level})

    return render(request,'testapp/exam.html',{'question':py_question,'type':'Python','level':level})




def java_exam(request):
    level = request.GET.get('level')
    py_question = Py_Question.objects.filter(level=level,type='java')
    if request.method == 'POST':
        score = 0
        total = py_question.count()
        result = []

        for q in py_question:
            valid = False
            user_answer = request.POST.get(f'question_{q.id}')
            user_answer_text='Not Attempted'

            if user_answer == q.correct_answer:
                score+=1
                valid = True
            if user_answer!=None:
                user_answer_text = str(user_answer)+'. '+str(getattr(q,'option_'+user_answer.lower()))

            result.append({'question':q.question_text,
                           'user_answer':user_answer_text,
                           'right_answer':str(q.correct_answer)+'. '+str(getattr(q,'option_'+str(q.correct_answer).lower())),
                           'valid':valid,
                           })
        return render(request,'testapp/result.html',{'result':result,'score':score,'total':total,'type':'Java','level':level})

    return render(request,'testapp/exam.html',{'question':py_question,'type':'Java','level':level})
def aptitude_exam(request):
    level = request.GET.get('level')
    py_question = Py_Question.objects.filter(level=level,type='frontend')
    if request.method == 'POST':
        score = 0
        total = py_question.count()
        result = []

        for q in py_question:
            valid = False
            user_answer = request.POST.get(f'question_{q.id}')
            user_answer_text='Not Attempted'
            
            if user_answer == q.correct_answer:
                score+=1
                valid = True
            if user_answer!=None:
                user_answer_text = str(user_answer)+'. '+str(getattr(q,'option_'+user_answer.lower()))

            result.append({'question':q.question_text,
                           'user_answer':user_answer_text,
                           'right_answer':str(q.correct_answer)+'. '+str(getattr(q,'option_'+str(q.correct_answer).lower())),
                           'valid':valid,
                           })
        return render(request,'testapp/result.html',{'result':result,'score':score,'total':total,'type':'Front-End','level':level})

    return render(request,'testapp/exam.html',{'question':py_question,'type':'Front-End Tech','level':level})
    


