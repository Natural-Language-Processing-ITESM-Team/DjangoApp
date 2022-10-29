from cgitb import text
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def chat(request):
    return render(request, 'core/chat.html')

def getTranscription(request):
    if request.method == 'POST':
        if 'text' in request.POST:
            args = {}
            text = request.POST['text']
            args['mytext'] = text
            print(args)
    return JsonResponse(args)
        
    