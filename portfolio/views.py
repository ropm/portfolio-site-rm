from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def portfolioView(request):
    return render(request, 'portfolio.html')