from django.shortcuts import render
import folium
import json
from decimal import Decimal
from requests import request
# Create your views here.
def addBusMarkers(map):
    result = request(method='get', url='http://back-service:8000/bus-stop/')
    bus_data = json.loads(result.content)
    icon_bus_url = 'https://cdn-icons-png.flaticon.com/512/7902/7902160.png'

    for bus in bus_data:  
        icon_bus  = folium.features.CustomIcon(icon_bus_url, icon_size=(50, 50)) 
        text = '<strong>Paradero</strong>: '+bus.get('name')
        folium.Marker(location=[Decimal(bus.get('latitude')), Decimal(bus.get('longitude'))], popup=text, icon=icon_bus).add_to(map)

def home(request):
    initialMap = folium.Map(location=[4.1486036,-73.6314936], zoom_start=13)
    initialMap._name = 'mimapa'
    initialMap._id = '8110'
    #agregando la posicion de los paraderos de buses
    addBusMarkers(initialMap)
    # Agregar Click listener a cada marcador
    for child in initialMap._children:
        if isinstance(child, folium.map.Marker):
            child.add_child(folium.ClickForMarker(popup='Clicked!'))
    icon_person_url = 'https://cdn-icons-png.flaticon.com/512/4151/4151463.png'
    context = {'map': initialMap._repr_html_, 'icon_person_url': icon_person_url}
    return render(request, 'map/home.html', context)    