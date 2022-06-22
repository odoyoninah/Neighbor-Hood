from django.conf import settings
from django.urls import path,include
from django.contrib import admin
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('account/', include('django.contrib.auth.urls')), 
    path('hoodbusiness/', views.hoodbusiness,name='hoodbusiness'),
    path('createbusiness/', views.createbusiness, name='createbusiness'),
    path('createpost/', views.createpost, name='createpost'),
    path('residence/', views.createhood, name='createhood'),
    path('hoodposts/', views.hoodposts,name='hoodposts' ),
    path('neighborhood/', views.neighborhood, name='neighborhood'),
    path('search/',views.search_name,name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)