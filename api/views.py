from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# ! Endpoints

def main(request):
   return HttpResponse("<h1>Hello Prince </h1>")

