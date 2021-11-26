import folium
import os

#Change the current directory to the folder
os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))) #this gets the current location reliably


map = folium.Map(location=[38.55,98.08], zoom_start=6)
map.save("index.html")

