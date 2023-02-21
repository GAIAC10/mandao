from django.urls import path
from .views import login_index

app_name = "mdauth"

urlpatterns = [
    path("login/",login_index, name="login"),

]