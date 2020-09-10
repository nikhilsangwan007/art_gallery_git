from django.urls import path

from . import views

app_name = 'art_gallery_app'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>/exhibition', views.ExhibitionView.as_view(), name='exhibition'),
    path('<int:exhibition_id>/collection', views.collection, name='collection'),
    path('paintings',views.paintings,name='all_paintings'),
    path('info',views.info,name='info'),
    path('<int:artist_id>/artwork',views.artwork,name='artwork'),
    path('query',views.query,name='query'),
    path('<int:query_id>/result',views.result,name='result'),
]