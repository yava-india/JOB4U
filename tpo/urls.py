from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='tpo-home'),
    path('administrator/', auth_views.LoginView.as_view(template_name='tpo/administrator.html'), name='tpo-administrator'),
    path('admin_panel', views.admin_panel, name='tpo-admin-panel'),
    #path('database', views.database, name='tpo-database'),
    path('google', views.google, name='tpo-google'),
    path('headstrait', views.headstrait, name='tpo-headstrait'),
    path('amazon', views.amazon, name='tpo-amazon'),
    path('amazondb',views.amazondb ,name='tpo-amazondb'),
    path('googledb',views.googledb ,name='tpo-googledb'),
    path('headstraitdb',views.headstraitdb ,name='tpo-headstraitdb'),
]


#auth_views.LoginView.as_view(template_name='tpo/administrator.html')
