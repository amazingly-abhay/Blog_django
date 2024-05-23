from django.shortcuts import render # type: ignore
from django.http import HttpResponse  # type: ignore #for http requests
from .models import Post


posts=[
    {
        'author':'Abhay',
        'title':'Blog 1',
        'content':'First post content',
        'date':'28 may, 2024'
    },
    {
        'author':'Akash',
        'title':'Blog 2',
        'content':'Second post content',
        'date':'29 may, 2024'
    },
    {
        'author':'Abhash',
        'title':'Blog 3',
        'content':'Third post content',
        'date':'30 may, 2024'
    }
]






# Create your views here.
def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'myapp/home.html',context)

def about(request):
    return render(request,'myapp/about.html',{"title":'About'})
