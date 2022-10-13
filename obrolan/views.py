from django.shortcuts import render

# Create your views here.
def show_obrolan(request):
    return render(request, "obrolan.html")