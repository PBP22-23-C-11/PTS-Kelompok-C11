from django.shortcuts import render

# Create your views here.
def show_showcase(request):
    return render(request, "showcase.html")