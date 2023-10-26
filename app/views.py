from django.shortcuts import render

# Create your views here.

def dz_22(request):
    data = ["apple", "banana", "cherry", "cucumber", "strawberries", "potato"]
    return render(request, "test.html", {"data": data})