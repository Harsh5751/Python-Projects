#import required libraries
import folium
import pandas
 
#read csv file and get required info from dataframe
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
 

#define color of marker based on elevation function
def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 < elevation < 3000:
        return "orange"
    else:
        return "red"

#Format string of elevation
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

#add objects using add_child; Adding markers with color coordinates and icon
map = folium.Map(location=[38.58, -99.09], zoom_start=4, tiles="Mapbox Bright")

#make featrue group of childs
#feature group for volcanoes
fgv = folium.FeatureGroup(name = "Volcanoes")
 
#for loop to add multiple points or markers
for lt, ln, el, name in zip(lat, lon, elev, name):
    #make a popup window on marker
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    #fill color for color inside marker and color for outline of marker
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=folium.Popup(iframe), fill_color = color_producer(el), color = "grey", fill_opacity = 0.7))

#make feature group for population
fgp = folium.FeatureGroup(name = "Population")

#adding another polygon layer on map to represent world population by color. Access population through properties dictionary
fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(), 
                            style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 
                                                        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

#add the feature groups to the map
map.add_child(fgp)
map.add_child(fgv)

#adding a legend for population
legend_html = """
    <div style="position: fixed; 
     bottom: 50px; left: 50px; width: 230px; height: 100px; 
     border:2px solid grey; z-index:9999; font-size:14px;
     background-color: white;
     ">&nbsp; <b>Population Legend</b> <br>
     &nbsp; <font color = "green">Pop < 10 000 000</font> &nbsp; <br>
     &nbsp; <font color = "orange">10 000 000 < Pop < 20 000 000</font>  &nbsp; <br>
     &nbsp; <font color = "red">Pop > 20 000 000</font> &nbsp; <br>
      </div>
"""

map.get_root().html.add_child(folium.Element(legend_html))

#add option toggle population and marker layer on or off
map.add_child(folium.LayerControl())

#save map object
map.save("Map.html")