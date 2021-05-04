from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('delivery/', views.delivery_detail, name='delivery_detail'),
    path('report/', views.report, name='report'),
]