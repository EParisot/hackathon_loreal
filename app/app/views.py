from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello l'Oreal. You're at the home page.")
