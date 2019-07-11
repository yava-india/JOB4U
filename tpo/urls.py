from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='tpo-home'),
    path('about/', views.about, name='tpo-about'),
    path('authenticate/', views.authenticate, name='tpo-authenticate'),
]
