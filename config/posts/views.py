from django.shortcuts import render
from django.views.generic import ListView
from . import models as M

class PostListView(ListView):
    model = M.Post
    template_name = 'home.html'

