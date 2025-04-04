
from django.urls import path

from . import views
app_name = "felviadmin"

urlpatterns = [
    path('', views.index, name='index'),
    path('addpage/',views.addPage, name="addPage"),
    path('addfelvetelizo',views.addFelvetelizo , name="addFelvetelizo"),
    path('delete/<int:felvetelizoId>',views.deleteFelvetelizo, name="deleteFelvetelizo"),

]
