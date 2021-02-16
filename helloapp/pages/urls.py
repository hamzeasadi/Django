from django.urls import path
from . import views as v

urlpatterns = [
    # path('', v.about, name='about')
    path('', v.AboutTemplateView.as_view(), name='about')
]