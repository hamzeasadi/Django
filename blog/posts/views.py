from django.shortcuts import render
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from . import models as M
from . import forms as F
from django.urls import reverse_lazy

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


class PostCreateView(CreateView):
    model = M.Post
    template_name = 'posts/create_post.html'
    form_class = F.CreatePostForm
    # fields = '__all__'
    # context_object_name = 'form'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostUpdateView(UpdateView):
    model = M.Post
    template_name = 'posts/update_post.html'
    context_object_name = 'form'
    # fields = ['title', 'content', 'date_posted']
    form_class = F.UpdatePostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostDeleteView(DeleteView):

    model = M.Post
    template_name = 'posts/delete_post.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')


