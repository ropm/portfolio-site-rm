from django.urls import path
from posts import views

urlpatterns = [
    path('', views.postsView, name='posts'),
    path('details/<int:id>', views.details, name='details'),    #simple regex = P parameter id, \d digit, +positive digit, $ end
]