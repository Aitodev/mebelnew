from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('design/', views.design, name='design'),
]
