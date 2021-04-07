from django.shortcuts import render

# Create your views here.
# will take the request, return index.html
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')