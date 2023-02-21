from django.urls import path
from .views import map_index,search_x_y
app_name = "map"
urlpatterns = [
    path("map/",map_index,name="map_index"),
    path("search_x_y/", search_x_y, name="search_x_y"),
]