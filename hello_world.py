import folium
import pandas

def initialize_map():
    return folium.Map(
        location = [40,-100],
        zoom_start = 5
    )


def load_volcanoes(path):
    return pandas.read_csv(path)


def place_marker_to_layer(marker, layer):
    layer.add_child(marker)


def iterate_through_data(data_volc):



my_map = initialize_map()
data_volc = load_volcanoes('Volcanoes_USA.txt')


my_map.save('usa.html')

