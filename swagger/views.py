from django.http import HttpResponse

def home(request):
    
    return HttpResponse('Home')


def signup(request):

    return HttpResponse('signup')


def login(request):

    return HttpResponse('login')        