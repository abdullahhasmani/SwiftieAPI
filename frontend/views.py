from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def quote(request):
    response = requests.get("https://swiftieapi-1-y1872095.deta.app/")
    data = response.json()
    print(data)
    return render(request,'hello.html',{'quote' : data['lyric'],'song':data['song']})