from django.shortcuts import render
from django.views.generic import TemplateView

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class HomeTemplateView(TemplateView):
    template_name = 'home.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

class AboutTemplateView(TemplateView):
    template_name = 'about.html'

