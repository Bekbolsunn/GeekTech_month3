from django.urls import path
from . import views

urlpatterns = [
   path('uhy/', views.blog_view)
]
