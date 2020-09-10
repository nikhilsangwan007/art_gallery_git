from django.urls import path

from . import views

app_name = 'art_gallery_app'

urlpatterns = [
	path('register/', views.RegisterView, name='register'),
	path('login/', views.LoginView, name='login'),
	path('logout/', views.LogutUser, name='logout'),
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>/exhibition', views.ExhibitionView.as_view(), name='exhibition'),
    path('<int:pk>/collection', views.CollectionView.as_view(), name='collection'),
]