from django.urls import path
from . import views

urlpatterns=[
    path('hello/', views.runFirstApi),
    
    # Auth 
    path('auth/signup/', views.authSignup)
]