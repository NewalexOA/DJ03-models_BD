from django.shortcuts import render

def index(request):
    return render(request, 'my_app/index.html')

def news(request):
    return render(request, 'news/news.html')

def contact(request):
    return render(request, 'my_app/contact.html')