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

# Create your views here.
