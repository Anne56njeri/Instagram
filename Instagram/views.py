from django.shortcuts import render

# Create your views here.
def index(request):
    title='Welcome to instagram'
    return render(request,'main/index.html',{"title":title})
