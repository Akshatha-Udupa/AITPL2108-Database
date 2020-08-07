#Map for different metrocity
import folium
import pandas
data = pandas.read_csv("metrocity1.csv")
city = list(data["City"])
long = list(data["Long"])
lat = list(data["Lat"])
color = list(data["Color"])
map = folium.Map(location=(12.58,77.48),zoom_start=5)
fg = folium.FeatureGroup(name="Map")
for lt, ln, clr, cty in zip(lat, long, color, city):
    fg.add_child(folium.Marker(location=(ln,lt), popup=cty, icon=folium.Icon(color=clr)))
map.add_child(fg)
map.save('mapnew.html')

