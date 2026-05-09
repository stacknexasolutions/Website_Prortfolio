from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

sitemaps = {}

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('api/chat/', views.chat_api, name='chat_api'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
]
