import folium
import os
import numpy
import pandas

#Change the current directory to the folder
os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))) #this gets the current location reliably
fileLocation = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

map = folium.Map(location=[39.01,-98.48], zoom_start=3)

fgv = folium.FeatureGroup(name="Volcanoes")
#For loop to insert coordinates
volcanoCoords = pandas.read_csv(os.path.join(fileLocation, "Volcanoes.txt"))

volcanoesLAT= list(volcanoCoords["LAT"])
volcanoesLON= list(volcanoCoords["LON"])
elevationData= list(volcanoCoords["ELEV"])

def color_produce(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <=elevation < 3000:
        return "orange"
    else:
        return "red"

html = """<h4>Volcano information:</h4>
Height: %s m

"""

#Nested for loop getting lat and long
for lat, lon, el in zip(volcanoesLAT,volcanoesLON, elevationData):
    
    fgv.add_child(folium.CircleMarker(location=[lat,lon], radius=6, popup=str(el) + " m", fill_color=color_produce(el), color="grey",fill=True, fill_opacity=0.7))

    #fg.add_child(folium.Marker(location=[lat,lon], popup=folium.Popup(iframe), icon=folium.Icon(color=color_produce(el)))) old markers
    #iframe = folium.IFrame(html=html % str(el), width=200, height=100)

fgp = folium.FeatureGroup(name="Population")


fgp.add_child(folium.GeoJson(data=open(os.path.join(fileLocation, "world.json"), 'r', encoding="utf-8-sig").read(), 
style_function=lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000  
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("index.html")

