from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models as M

class PostListView(ListView):
    model = M.Post
    context_object_name = 'posts'
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetailView(DetailView):
    model = M.Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



