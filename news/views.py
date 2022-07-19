from django.shortcuts import render,redirect
from .models import Artik
from .forms import ArtikFrom

def news_home(request):
    news=Artik.objects.order_by("-date")
    return  render(request,'news/news.html',{"news":news})

def create(request):
    eror=''
    if request.method=='POST':
        form=ArtikFrom(request.post)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            eror="форма не верная "
    form=ArtikFrom()

    date ={
        'form':form,
        'eror':eror
    }
    return  render(request,"news/create.html",date)