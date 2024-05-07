from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def homepage(request):
#      return HttpResponse("Hello World! I'm Home.")
      return render(request, 'home.html')

def about(request):
#    return HttpResponse("My About Page")
     return render(request, 'about.html')