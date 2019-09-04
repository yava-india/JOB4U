from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='tpo-home'),
    path('about', views.about, name='tpo-about'),
    path('administrator/', auth_views.LoginView.as_view(template_name='tpo/administrator.html'), name='tpo-administrator'),
    path('admin_panel', views.admin_panel, name='tpo-admin-panel'),
    path('database', views.database, name='tpo-database'),
]


#auth_views.LoginView.as_view(template_name='tpo/administrator.html')
