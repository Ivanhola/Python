import folium
import os
import numpy
import pandas

#Change the current directory to the folder
os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))) #this gets the current location reliably
fileLocation = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

map = folium.Map(location=[39.01,-98.48], zoom_start=3)

fg = folium.FeatureGroup(name="My Map")
#For loop to insert coordinates
volcanoCoords = pandas.read_csv(os.path.join(fileLocation, "Volcanoes.txt"))

volcanoesLAT= list(volcanoCoords["LAT"])
volcanoesLON= list(volcanoCoords["LON"])
elevationData= list(volcanoCoords["ELEV"])

#Nested for loop getting lat and long
for lat, lon, el in zip(volcanoesLAT,volcanoesLON, elevationData):
    fg.add_child(folium.Marker(location=[lat,lon], popup=str(el) + " m.", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("index.html")

