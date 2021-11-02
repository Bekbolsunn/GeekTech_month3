import datetime
from typing import List
from django.shortcuts import render
from django.http.request import HttpRequest
from .models import BlogPost


def blog_view(request):
    post = BlogPost.objects.all()
    return render(request, 'index.html', context={'blogs': post})

# def date_view(request):
#     date = datetime.datetime.now()
#     return HttpResponse(f'Сейчас {date}')