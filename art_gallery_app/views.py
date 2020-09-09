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


class ExhibitionView(generic.ListView):
	template_name = 'art_gallery/exhibition.html'
	context_object_name = 'exhibition_list'
	
	def get_queryset(self):
		pk = self.kwargs['pk']
		ex_list = DbExhibition.objects.filter(gallery=pk)
		return ex_list

class CollectionView(generic.ListView):
	template_name = 'art_gallery/collection.html'
	context_object_name = 'context_painting_list'

	def get_queryset(self):
		pk = self.kwargs['pk']
		painting_id_list = DbExhibitionPainting.objects.filter(exhibition=pk)
		context_painting_list = {}
		for ids in painting_id_list:
			painting_list = DbPainting.objects.filter(painting_id = ids.painting.painting_id)
		context_painting_list['painting_list'] = painting_list
		return context_painting_list

# Create your views here.
