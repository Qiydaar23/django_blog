from django.shortcuts import render
from django.http import HttpResponse


posts =[
    {
        'author':'Qiydaar',
        'title':'Blog Post 1',
        'content': 'First post content',
        'date_posted':'August 23, 2024'
    },
        {
        'author':'ryan gibbs',
        'title':'Blog Post 2',
        'content': 'second post content',
        'date_posted':'August 24, 2024'
    }
]




def home(request):
    context ={
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

