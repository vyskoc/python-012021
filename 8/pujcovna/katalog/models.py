from django.db import models

class Auto(models.Model):
    rz = models.CharField(max_length=7)
    znacka = models.CharField(max_length=100)
    km = models.IntegerField()
    tk = models.DateField()

class Zakaznik(models.Model):
    jmeno = models.CharField(max_length=25)
    prijmeni = models.CharField(max_length=100)
    ridicsky_prukaz = models.CharField(max_length=15)
    datum_narozeni = models.DateField()

class Vypujcka(models.Model):
    vypujceni = models.DateTimeField()
    vraceni = models.DateTimeField()
    cena = models.IntegerField()