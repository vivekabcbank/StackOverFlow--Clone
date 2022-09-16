from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "help"

urlpatterns = [
    path("privileges/", views.privileges, name="privileges"),
]
