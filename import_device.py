#!/usr/bin/env python
from __future__ import print_function
import erppeek
import csv

marques = {}

client = erppeek.Client.from_config('test')

def verifMarque(marque):
    if marque not in marques:
        proxy = client.model('iut.it.brand')
        requette = proxy.search(name=marque)
        if requette==null:
            

with open('devices.csv', newline='') as fichiercsv:
    tableau = csv.reader(fichiercsv)
    for ligne in tableau:
        numSerieLigne = ligne[0]
        dateAlloLigne = ligne[1]
        dateAchatLigne = ligne[2]
        modeleLigne = ligne[3]
        type = ligne[5]
        employe = ligne[6]

proxy = client.model('iut.it.device')

devices = proxy.browse([6,7,9])

for device in devices:
    print("{device.id} {device.name}".format(device=device))
