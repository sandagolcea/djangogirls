from django.shortcuts import render

# Create your views here.
def geolocation(request):
    # request, html name, any params {}
    return render(request, 'geolocation.html', {})
