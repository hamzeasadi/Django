from django.urls import path
from . import views as V

urlpatterns = [
    path('', V.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', V.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', V.PostCreateView.as_view(), name="new-post"),
    path('post/<int:pk>/update/', V.PostUpdateView.as_view(), name='update-post'),
    path('post/<int:pk>/delete/', V.PostDeleteView.as_view(), name='delete-post')
]