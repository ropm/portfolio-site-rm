from django.urls import path
from . import views

urlpatterns = [
    path('',views.postsView, name='posts'),
]