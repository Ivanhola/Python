import folium
import os
import numpy
import pandas

#Change the current directory to the folder
os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))) #this gets the current location reliably
fileLocation = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

map = folium.Map(location=[38.55,98.08], zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
#For loop to insert coordinates
volcanoCoords = pandas.read_csv(os.path.join(fileLocation, "Volcanoes.txt"))

volcanoesLAT= list(volcanoCoords.loc[:,"LAT"])
volcanoesLON= list(volcanoCoords.loc[:,"LON"])


#Nested for loop getting lat and long
for lat in volcanoesLAT:
    for lon in volcanoesLON:
        
        fg.add_child(folium.Marker(location=[lat,lon], popup="I'm a marker", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("index.html")

