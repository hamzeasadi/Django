from django.urls import path
from . import views as V

urlpatterns = [
    path('', V.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', V.PostDetailView.as_view(), name='post-detail')
]