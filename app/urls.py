from django.urls import path
from app.views import addTuto, tutoPage, updateTuto, upd_del_tuto,connexion,listTutos
urlpatterns = [
    path("list", listTutos, name="list"),
    path("tuto/ajout",addTuto,name="tutoajout"),
    path("tuto/<str:idTuto>/update", updateTuto, name = "update"),
    path("tuto/<str:idTuto>/upd-del", upd_del_tuto, name = "updatedeletetuto"),
    path("", connexion, name="connexion"),
    path("tuto/<str:idTuto>",tutoPage, name="tuto"),
]