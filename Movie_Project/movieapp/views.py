from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from.models import Movie
# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"details.html",{'movie':movie})
from django.http import HttpResponse



def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name', None)
        desc = request.POST.get('desc', None)
        year = request.POST.get('year', None)
        img = request.FILES.get('img', None)

        if name and desc and year and img:
            movie = Movie(name=name, desc=desc, year=year, img=img)
            movie.save()
            return render(request, 'add.html')  
        return HttpResponse(
            "<center><h2>Please enter all the fields correctly!!</h2><br><a href='/add' class='btn btn-primary' >cancel & go back?</a></center>"
        )

    return render(request, 'add.html')



def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
