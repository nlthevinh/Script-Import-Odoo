#!/usr/bin/env python
from __future__ import print_function
import erppeek
import csv
from docutils.nodes import row
from mimetypes import add_type


client = erppeek.Client.from_config('test')

device = client.model('iut.it.device')
brand = client.model('iut.it.brand')
model = client.model('iut.it.model')
model_type = client.model('iut.it.modeltype')
partner = client.model('res.partner')

types = []

def recherche_device(num):
    recherche_devices = device.search([('serial_number', '=', num)])
    return device.browse(recherche_devices)

def recherche_device_all():
    recherche_devices = device.search([])
    return device.browse(recherche_devices)

def recherche_brand(nom):
    recherche_brands = brand.search([('name', '=', nom)])
    return brand.browse(recherche_brands)

def recherche_model(nom):
    recherche_models = model.search([('name', '=', nom)])
    return model.browse(recherche_models)

def recherche_model_types(nom):
    recherche_model_types = model_type.search([('name', '=', nom)])
    return model_type.browse(recherche_model_types)

def recherche_partner(nom):
    recherche_partners = partner.search([('name', '=', nom)])
    return partner.browse(recherche_partners)

def check_device(str):
    if recherche_device(str).serial_number == []:
        return False
    else:
        return True

def check_brands(str):
    if recherche_brand(str).name == []:
        brand.create({'name':str}) 
         
def check_model(str):
    if recherche_model(str).name == []:
        model.create({'name': str}) 
        
def check_partner(str):
    if recherche_partner(str).name == []:
        partner.create({'name':str}) 

def check_types(str):
    types = str.split(':')
                        
    for type in types:   
        if recherche_model_types(type).name == []:
            model_type.create({'name':type})

def get_id_type(str): 
    id = []
    types = str.split(':')
                        
    for type in types:
        if recherche_model_types(type) == []:
            id.append(recherche_model_types(type))
    return id

def ajouter_type(str):
        a = check_model(str)
        model.write(a, {'type_ids': get_id_type(str)}) 
        
def ajouter_device_a_partner(str, device):
        a = check_partner(str)
        partner.write(a, {'device_ids': device}) 
        
with open('./test.csv', newline='') as fichier_csv:
    spamreader = csv.reader(fichier_csv, delimiter=';', quotechar='|')
    
    for row in spamreader:                   
        check_brands(row[5])                 
        check_model(row[4])      
        check_types(row[6]) 
        ajouter_type(row[4])      
        check_partner(row[7])                
                    
        if check_device(row[1]):
            evice.create({'name':row[0], 'serial_number': row[1], 'date_allocation':row[2], 'date_purshase': row[3], 'id_model': recherche_model(row[4]).ID()}) 
        
        ajouter_device_a_partner(row[7], row[1])
