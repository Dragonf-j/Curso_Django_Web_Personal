from django.shortcuts import render, HttpResponse




# Create your views here.
def home(request):
   # return HttpResponse(html_Base+"<h2>Portada</h2>")
    return render(request, "core/home.html")
   
def about(request):
    return render(request, "core/about.html")
def contacto(request):
    return render(request, "core/contact.html")
