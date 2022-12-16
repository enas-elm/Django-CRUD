from django.shortcuts import render

# from .models import Question

def index(request):
    return render(request, 'app/index.html')
