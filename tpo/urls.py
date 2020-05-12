from django.urls import path
# from .import views
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('administrator/', auth_views.LoginView.as_view(template_name='tpo/administrator.html'), name='tpo-administrator'),
    path('admin_panel', views.admin_panel, name='tpo-admin-panel'),
    #path('database', views.database, name='tpo-database'),
    path('', views.index, name='tpo-index'),
    path('robots.txt', views.index, name='tpo-index'),
    path('temp', views.webcsv10may, name='csv-index'),
    path('lti', views.ltionlymap, name='tpo-lti'),
    path('Wipro', views.wiproonlymap, name='tpo-lti'),
    # path('lti', views.newlti, name='tpo-lti'),
    path('virtusa', views.harm, name='tpo-harm'),
    path('imageworngResult', views.capgresult, name='tpo-harm'),
    path('CapgeminiDiversityResult', views.cgdiv, name='tpo-harm'),
    path('Tolearn', views.Tolearn, name='tpo-Tolearn'),
    path('infosys15nov', views.Infosys, name='tpo-infosys'),
    path('Ltiresult', views.Lti12result, name='tpo-ltiresult'),
    path('Paytm', views.paytm, name='tpo-cap'),
    path('SwabhavTechlabs', views.swabhav, name='tpo-cap'),
    path('infosys', views.Infosys, name='tpo-infosys'),
    path('amazondb',views.amazondb ,name='tpo-amazondb'),
    path('lti20novdb',views.lti20db ,name='tpo-lti20nov'),
    path('infosys15novdb',views.info15novdb ,name='tpo-lti20nov'),
    path('googledb',views.googledb ,name='tpo-googledb'),
    path('headstraitdb',views.headstraitdb ,name='tpo-headstraitdb'),
    path('a_1_Salasardb', views.a_1_Salasardb, name='tpo-a1salasar'),
    path('ltidb',views.lti_db ,name='tpo-ltidb'),
    path('Cap8jandb',views.cap8jandb ,name='tpo-ltidb'),
    path('Qualitykiosk',views.quality ,name='tpo-quality'),
    path('ibmdb',views.ibmdatabase ,name='tpo-ibmdb'),
    # path('swabhav12decdb',views.swab1212db ,name='tpo-ibmdb'),
    path('wonder6mardb',views.swab1212db ,name='tpo-ibmdb'),
    path('bit9decdb',views.bit912db ,name='tpo-ibmdb'),
    path('cap20novdb',views.cap20db ,name='tpo-ibmdb'),
    path('capgemini8jan',views.capgemini8jan ,name='tpo-ibmdb'),
    path('capgemini10jan',views.capgemini10jan ,name='tpo-ibmdb'),
    path('cc',views.webinar ,name='tpo-ibmdb'),
    path('web10maydb',views.web1005db ,name='tpo-ibmdb'),
    path('Lti14jandb',views.zycus11jandb ,name='tpo-ibmdb'),
    path('Ibm',views.ibm27feb ,name='tpo-ibmdb'),
    path('lti28novdb',views.lti2811db ,name='tpo-mdb'),
    path('virtusadb',views.virtusadatabase ,name='tpo-ibmdb'),
    path('virt11mardb',views.virt1103db ,name='tpo-ibmdb'),
    path('zycusdb',views.zycusdatabase ,name='tpo-ibmdb'),
    path('infosysdb15',views.info15database ,name='tpo-info15db'),
    path('infosysdb16',views.info16database ,name='tpo-info16db'),
    path('ibmdb7',views.newibmdatabase ,name='tpo-ibmdb'),
    path('result',views.thank ,name='tpo-result'),
    # path('zycus',views.Infosys ,name='tpo-result'),
    path('ibmresult',views.IBmresult ,name='tpo-ibmresult'),
    path('Capgeminiiiii',views.cap20novresult ,name='tpo-capresult'),
    path('ZycusList',views.cap25novresult ,name='tpo-capresult'),
    path('VirtusaSlots',views.cap19novdata ,name='tpo-capdata'),
    path('infosysresult',views.INfosys16result ,name='tpo-inforeslt'),
    path('infosysfinalresultscolleges',views.Infofinalresult ,name='tpo-infohhreslt'),
    path('CapgeminiResults',views.zycusaptilist ,name='tpo-infohhreslt'),
    path('WonderBizRS',views.wonderbiz ,name='tpo-wonderbiz'),
    path('infosysfinalresult',views.Infofinalnameresult ,name='tpo-infohnamehreslt'),
    path('infosys15result',views.INfosys15result ,name='tpo-inf3oreslt'),

]


#auth_views.LoginView.as_view(template_name='tpo/administrator.html')
