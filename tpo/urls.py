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
    path('', views.index, name='tpo-index'),
    # path('temp', views.index, name='tpo-index'),
    # path('lti', views.lti, name='tpo-lti'),
    path('lti', views.newlti, name='tpo-lti'),
    path('virtusa', views.harm, name='tpo-harm'),
    path('Tolearn', views.Tolearn, name='tpo-Tolearn'),
    path('infosys15nov', views.Infosys, name='tpo-infosys'),
    path('amazondb',views.amazondb ,name='tpo-amazondb'),
    path('googledb',views.googledb ,name='tpo-googledb'),
    path('headstraitdb',views.headstraitdb ,name='tpo-headstraitdb'),
    path('a_1_Salasardb', views.a_1_Salasardb, name='tpo-a1salasar'),
    path('ltidb',views.lti_db ,name='tpo-ltidb'),
    path('VIRTUSA',views.ibm ,name='tpo-infosys'),
    path('ibmdb',views.ibmdatabase ,name='tpo-ibmdb'),
    path('virtusadb',views.virtusadatabase ,name='tpo-ibmdb'),
    path('zycusdb',views.zycusdatabase ,name='tpo-ibmdb'),
    path('infosysdb15',views.info15database ,name='tpo-info15db'),
    path('infosysdb16',views.info16database ,name='tpo-info16db'),
    path('ibmdb7',views.newibmdatabase ,name='tpo-ibmdb'),
    path('result',views.thank ,name='tpo-result'),
    path('zycus',views.Infosys ,name='tpo-result'),
    path('ibmresult',views.IBmresult ,name='tpo-ibmresult'),
    path('infosysresult',views.INfosys16result ,name='tpo-inforeslt'),
    path('infosysfinalresultscolleges',views.Infofinalresult ,name='tpo-infohhreslt'),
    path('infosysfinalresult',views.Infofinalnameresult ,name='tpo-infohnamehreslt'),
    path('infosys15result',views.INfosys15result ,name='tpo-inf3oreslt'),

]


#auth_views.LoginView.as_view(template_name='tpo/administrator.html')
