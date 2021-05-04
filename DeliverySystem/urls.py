"""DeliverySystem path Configuration

The `pathpatterns` list routes paths to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a path to pathpatterns:  path('$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a path to pathpatterns:  path('$', Home.as_view(), name='home')
Including another pathconf
    1. Import the include() function: from django.conf.paths import path, include
    2. Add a path to pathpatterns:  path('blog/', include('blog.paths'))
"""
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static

from registration import views as registration_views
from registration.forms import ContactForm

from rest_framework import routers

router = routers.DefaultRouter()
router.register('delivery', registration_views.DeliveryViewSet)

urlpatterns = [
    #Django-Jet paths
	path('jet/', include('jet.urls', 'jet')),
	path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    
    #Django default paths
    path('admin/', admin.site.urls, name='admin'),
    path('', include('registration.urls', namespace='registration')),
    path('news/', include('news.urls', namespace='news')),
    path('api/', include(router.urls)),

    #Django-AllAuth paths
    path('accounts/', include('allauth.urls')),

    #ContactForm paths
    path('contact-us/', registration_views.contact_us, name='contact-us'),
    path('thanks/', registration_views.thanks, name='thanks'),
    
    #Report paths
    path('report_builder/', include('report_builder.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
