from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("<h1>Welcome to CBVs World</h1>")