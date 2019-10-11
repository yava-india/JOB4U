from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path('', views.index, name='tpo-home'),
    path('administrator/', auth_views.LoginView.as_view(template_name='tpo/administrator.html'), name='tpo-administrator'),
    path('admin_panel', views.admin_panel, name='tpo-admin-panel'),
    #path('database', views.database, name='tpo-database'),
    #path('google', views.google, name='tpo-google'),
    #path('headstrait', views.headstrait, name='tpo-headstrait'),
    #path('amazon', views.amazon, name='tpo-amazon'),
    path('', views.lti, name='tpo-index'),
    path('temp', views.index, name='tpo-index'),
    path('lti', views.lti, name='tpo-lti'),
    path('amazondb',views.amazondb ,name='tpo-amazondb'),
    path('googledb',views.googledb ,name='tpo-googledb'),
    path('headstraitdb',views.headstraitdb ,name='tpo-headstraitdb'),
    path('a_1_Salasardb', views.a_1_Salasardb, name='tpo-a1salasar'),
    path('ltidb',views.lti_db ,name='tpo-ltidb'),
    path('Ibm',views.ibm ,name='tpo-ibm'),
    path('ibmdb',views.ibmdatabase ,name='tpo-ibmdb'),
    path('ibmdb7',views.newibmdatabase ,name='tpo-ibmdb'),
    path('result',views.thank ,name='tpo-result'),
    path('infosys',views.Infosys ,name='tpo-result'),
    path('ibmresult',views.IBmresult ,name='tpo-ibmresult'),
]


#auth_views.LoginView.as_view(template_name='tpo/administrator.html')
