from django.http import HttpResponse
from Routes.models import*
from utilities import *
import json

# Placeholder
def index(request):
    return HttpResponse("Welcome to Routes!")

def concord(request):
    dic = json.loads(request.body)
    return dic

# Occurs when traveler matches a ConcreteRoute
def match(request):
    dic = concord(request)
    user = dic['user']
    c_route = ConcreteRoute.objects.filter(id=dic['route'])
    traveler = Traveler.objects.filter(user=request.user())

    c_route.match(traveler)

    return HttpResponse("Route matched. Aproval pending.")

# Occurs when guide confirms a ConcreteRoute match
def confirmMatch(request):
    if not request.user.is_authenticated():
        exit()

    dic = concord(request)

    id_route = dic['route']
    guide = Guide.objects.filter(user=request.user())

    p = APRoute.objects.filter(guide=guide, route=id_route)
    p.confirmMatch()

    return HttpResponse("Match confirmed by guide!!!")


def search(request):

    if not request.user.is_authenticated():
        exit()

    dic = concord(request)

    country = dic['pais']
    POI = dic['POI']
    language = dic['language']

    routes = list(ConcreteRoute.objects.filter(route__country=country, language__in=json.loads(route__guide__languages)),POI.keys() in route__pointsOfInterest)
    return HttpResponse(json.dumps(routes))