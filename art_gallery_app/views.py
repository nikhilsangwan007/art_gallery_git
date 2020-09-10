# from django.http import HttpResponseRedirect 
# from django.shortcuts import get_object_or_404 
# from django.shortcuts import render
# from django.urls import reverse
# from django.views import generic
# from django.http import Http404 
# from django.db import connection
# from .models import DbArtist, DbExhibition, DbExhibitionPainting, DbGallery, DbPainting,DbQueries

app_name = 'art_gallery_app'

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

 from .form import *
from .models import *

def RegisterView(request):
	if request.user.is_authenticated:
		return redirect('art_gallery_app:home')
	else:
		form = CreateUserForm()

		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				messages.success(request, 'Account created successfully')
				return redirect('art_gallery_app:login')
			else:
				messages.success(request, 'Failed')

		context = {'form': form}
		return render(request, 'art_gallery/register.html', context)


def LoginView(request):
	if request.user.is_authenticated:
		return redirect('art_gallery_app:home')
	else:
		context = {}
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('art_gallery_app:home')
			else:
				messages.info(request, 'username or password is incorrect')
				# return render(request, 'art_gallery/login.html', context)

		return render(request, 'art_gallery/login.html', context)


def LogutUser(request):
	logout(request)
	return redirect('art_gallery_app:home')

# @login_required(login_url='art_gallery_app:login')
class HomeView(generic.ListView):
	template_name = 'art_gallery/home.html'
	context_object_name = 'gallery_list'

	def get_queryset(self):
	    return DbGallery.objects.all()

# @login_required(login_url='art_gallery_app:login')
class ExhibitionView(generic.ListView):
	template_name = 'art_gallery/exhibition.html'
	context_object_name = 'exhibition_list'
	
	def get_queryset(self):
		pk = self.kwargs['pk']
		ex_list = DbExhibition.objects.filter(gallery=pk)
		return ex_list


# @login_required(login_url='art_gallery_app:login')
class CollectionView(generic.DetailView):
	template_name = 'art_gallery/collection.html'
	context_object_name = 'context_painting_list'
	model = DbExhibitionPainting

	def get_queryset(self):
		pk = self.kwargs['pk']
		paint_list = DbExhibitionPainting.objects.filter(exhibition=pk)
		return paint_list

def collection(request , exhibition_id):
	try :
		painting_ids = DbExhibitionPainting.objects.filter(exhibition=exhibition_id)
	except DbExhibitionPainting.DoesNotExist:
		raise Http404("Exhibition does not exist")
	data = []
	for pid in painting_ids:
		paintingInfo = DbPainting.objects.get(pk=pid.painting_id)
		data.append(paintingInfo)
	# print(data)
	return render(request,'art_gallery/collection.html',{ 'data' :data })
# Create your views here.
def paintings(request):
	paintings_data = DbPainting.objects.all()
	# print(data)
	return render(request,'art_gallery/paintings.html',{'paintings':paintings_data})

def info(request):
	artists = DbArtist.objects.all()
	return render(request,'art_gallery/info.html',{'artists':artists})

def artwork(request,artist_id):
	paintings = DbPainting.objects.filter(artist=artist_id)
	return render(request , 'art_gallery/artwork.html',{'paintings' :paintings})

def query(request):
	queryList = DbQueries.objects.all()
	return render(request,'art_gallery/query.html',{'queryList':queryList})

def result(request , query_id):
	query = DbQueries.objects.get(pk=query_id)
	with connection.cursor() as cursor:
		cursor.execute(query.query)
		row = cursor.fetchall()
	return render(request ,'art_gallery/result.html',{'row':row})

