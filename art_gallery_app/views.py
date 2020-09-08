from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import DbArtist, DbExhibition, DbExhibitionPainting, DbGallery, DbPainting

class HomeView(generic.ListView):
	template_name = 'art_gallery/home.html'
	context_object_name = 'gallery_list'

	def get_queryset(self):
	    return DbGallery.objects.all()

# Create your views here.
