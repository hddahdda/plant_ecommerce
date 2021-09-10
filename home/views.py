from django.shortcuts import render

# Create your views here.


def index(request):
    """ Home/landing page view """

    return render(request, 'home/index.html')
