# capa de servicio/lógica de negocio

from ..persistence import repositories
from ..utilities import translator
from ..transport import transport
from django.contrib.auth import get_user


def getAllImages(input=None):
    # obtiene un listado de datos "crudos" desde la API, usando a transport.py.
    json_collection = transport.getAllImages(input)

    # recorre cada dato crudo de la colección anterior, lo convierte en una Card y lo agrega a images.
    images = []
    for i in range(len(json_collection)):
        image = translator.fromRequestIntoCard(json_collection[i])
        images.append(image)

    return images

# añadir favoritos (usado desde el template 'home.html')


def saveFavourite(request):
    # transformamos un request del template en una Card.
    fav = translator.fromTemplateIntoCard(request)
    fav.user = get_user(request)  # le asignamos el usuario correspondiente.

    return repositories.saveFavourite(fav)  # lo guardamos en la base.

# usados desde el template 'favourites.html'


def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)
        # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        favourite_list = repositories.getAllFavouritesByUser(user)
        mapped_favourites = []

        for favourite in favourite_list:
            # transformamos cada favorito en una Card, y lo almacenamos en card.
            card = ''
            mapped_favourites.append(card)

        return mapped_favourites


def deleteFavourite(request):
    # Elimina un favorito por el usuario
    favId = request.POST.get('id')
    # borramos un favorito por su ID.
    return repositories.deleteFavourite(favId)
