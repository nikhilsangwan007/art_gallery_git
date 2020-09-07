from django.urls import path

from . import views

app_name = 'art_gallery_app'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]