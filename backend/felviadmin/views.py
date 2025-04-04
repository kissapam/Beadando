from django.shortcuts import render, redirect

from .models import Szak,Felvetelizo

# Create your views here.
def index(request):
    osszesAdat = Felvetelizo.objects.all().order_by("-szulEv")
    context = {"adatok":osszesAdat}
    return render (request, "index.html", context)

# két view-t hozok létre a felvitelhez (egyik lerendeli az ürlap oldalt, a másik feldolgozza az adatokat)
def addPage(request):   # az elsőben a renderelést oldom meg, kell a legördülő listához a szakok listája ezért:
    osszesSzak = Szak.objects.all().order_by("szakNev")
    context = {"szakok":osszesSzak}
    return render(request,"add.html", context)

# az ürlapból megkapja az adatokat és az adatbázisba rögzíti
def addFelvetelizo(request):
    if request.method == "POST":
        _szakId = request.POST["szak_valaszt"]
        _szak = Szak.objects.get(pk=_szakId)
        _nev = request.POST["nev"]
        _szulEv = request.POST["szulEv"]
        _pontszam = request.POST["pontszam"]
        newFelvetelizo = Felvetelizo(szakId = _szak, nev = _nev, szulEv = _szulEv, pontszam = _pontszam)
        newFelvetelizo.save()
    return redirect("/")    

#  a törlés leírása
def deleteFelvetelizo(request,felvetelizoId):
    if request.method == "POST":
        current = Felvetelizo.objects.get(pk=felvetelizoId)
        current.delete()
    return redirect("/")


