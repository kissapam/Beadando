from django.shortcuts import render, redirect
# kép beolvasásához fájl-ból kell importálni a következő sort
from django.core.files.storage import FileSystemStorage

from .models import Szak,Felvetelizo

# Create your views here
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
    if request.method == "POST" and request.FILES["kep"]: # az end és ami ztánna van a képfeltöltéshez kell
        _szakId = request.POST["szak_valaszt"]
        _szak = None # Az if-en belüli _szak változó nem lenne látható késöbb a felvételiző összeállításáshoz így előbb deklarálom
        if _szakId == "addSzak": # ha a szakId-nak az addSzak értéket kaptam (mert az ürlapon új szakot adok hozzá) akkor
            _ujSzak = request.POST["ujSzak"] # a kapott új szakot "ujSzak" fel kell vinni az adatbázisba
            aktUjSzak = Szak(szakNev = _ujSzak, tamogatott = False) # itt állítom össze egy aktuális új szak objektumban
            aktUjSzak.save() # itt mentem el a Szak modelben (táblában)
            _szak = aktUjSzak # a felvételiző összeállításához pedig továbbítom az új szakot
        else:
            _szak = Szak.objects.get(pk=_szakId) # már meglévő szak lett kiválasztva, ez az id megy tovább a felvételiző összeállításához
        _nev = request.POST["nev"]
        _szulEv = request.POST["szulEv"]
        _pontszam = request.POST["pontszam"]
        # itt adom a képet az új felvételizőhöz
        _kepAdatok = request.FILES["kep"]
        fs = FileSystemStorage()
        _kep = fs.save(_kepAdatok.name, _kepAdatok)

        # és itt állítom össze az új példányt az osztályból
        newFelvetelizo = Felvetelizo(szakId = _szak, nev = _nev, szulEv = _szulEv, pontszam = _pontszam, kep = _kep)
        newFelvetelizo.save()
    return redirect("/")    

#  a törlés leírása
def deleteFelvetelizo(request,felvetelizoId):
    if request.method == "POST":
        current = Felvetelizo.objects.get(pk=felvetelizoId)
        current.delete()
    return redirect("/")


