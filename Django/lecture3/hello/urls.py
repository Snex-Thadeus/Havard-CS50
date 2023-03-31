from django.urls import path
from .  import views


urlpatterns = [
    path("", views.index, name="index"),
    path("snex", views.snex, name="snex"),
    path("<str:name>", views.greet, name="greet")
]