from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


# Create your views here.
class HomePage(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Pagina de inicio')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')


class Home(generic.TemplateView):
    template_name = "generales/home.html"
