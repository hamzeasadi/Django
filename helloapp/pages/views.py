from django.shortcuts import render
from django.views.generic import TemplateView
# function based view
def about(request):
    return render(request, 'pages/about.html')

# class based view
class AboutTemplateView(TemplateView):
    template_name = 'pages/about.html'
