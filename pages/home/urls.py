from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.HomeTemplateView.as_view(), name='home'),
    path('about/', v.AboutTemplateView.as_view(), name='about')
]
