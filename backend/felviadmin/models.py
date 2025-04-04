from django.db import models

# Create your models here.

class Szak(models.Model):
    szakNev = models.CharField(max_length=100)
    tamogatott = models.BooleanField(default=False)

    def __str__(self):
        return self.szakNev
    class Meta:
        verbose_name_plural = "Szakok"
    
class Felvetelizo(models.Model):
    szakId = models.ForeignKey("Szak",on_delete=models.CASCADE)
    nev = models.CharField(max_length=100)
    szulEv = models.IntegerField()
    pontszam = models.IntegerField()
    kep = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return f"{self.nev} ( {self.pontszam})"
    
    class Meta:
        verbose_name_plural = "Felvételizők"
    