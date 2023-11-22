from django.shortcuts import render

# Create your views here.
def person(request):
    return render(request,'person.html')