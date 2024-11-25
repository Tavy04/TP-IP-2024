# capa de vista/presentación

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .layers.services import services

# Página inicial


def index_page(request):
    return render(request, 'index.html')

# Muestra la página principal con las imágenes y los favoritos


def home(request):
    images = services.getAllImages()

    favourite_list = []
    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list})

# Realiza búsquedas de personajes


def search(request):
    search_msg = request.POST.get('query', '')
  # si el texto ingresado no es vacío, trae las imágenes y favoritos desde services.py,

    if (search_msg != ''):
        images = services.getAllImages(search_msg)
        favourite_list = []

        return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list})
    else:
        return redirect('home')

# Muestra los favoritos del usuario autenticado.


@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    favourite_list = services.getAllImages()

    return render(request, 'favourites.html', {'favourite_list': favourite_list})


@login_required
def saveFavourite(request):
    pass


@login_required
def deleteFavourite(request):
    pass


@login_required
def exit(request):
    logout(request)
    return render(request, 'index.html')
