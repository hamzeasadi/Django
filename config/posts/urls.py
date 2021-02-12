from django.urls import path
from . import views as views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home')
]