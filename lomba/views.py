from django.shortcuts import render

# Create your views here.
def show_lomba(request):
    return render(request, "lomba.html")