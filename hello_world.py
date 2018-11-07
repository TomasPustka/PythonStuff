import folium
import pandas


def initialize_map():
    return folium.Map(
        location=[40,-100],
        zoom_start=5
    )


def load_volcanoes(path):
    return pandas.read_csv(path)


def place_marker_to_layer(marker, layer):
    layer.add_child(marker)


def marker_code_based_on_height(height):
    if height < 2000:
        return 'green'
    elif 2000 <= height < 3000:
        return 'orange'
    else:
        return 'red'

def iterate_through_data(base_map, data_frame):

    for row in data_frame.itertuples():
        #print(row[0], row[6])
        folium.Marker(location=[row[9], row[10]], icon=folium.Icon(color=marker_code_based_on_height(int(row[6])))).add_to(base_map)


my_map = initialize_map()
data_volc = load_volcanoes('Volcanoes_USA.txt')
iterate_through_data(my_map, data_volc)
my_map.save('usa.html')

