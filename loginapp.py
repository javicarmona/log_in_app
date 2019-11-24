#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 00:51:19 2019

@author: javiercarmona
"""

import datetime
import pandas as pd
import pickle #pickle is a module to save .dat files

"""
Log in open de dictionary from the dat file.
Check if the user name is on the database and ask for password.
"""
def login(uname):
    USACdb = cargar_datos()
    if uname in USACdb:
        password = input ('Welcome, please introduce password: ')
        passwordx = hash(password)
        if passwordx == USACdb[uname][0]:
            print ('Welcome to USAC')
        else:
            print ('Password invalid, sorry.')
    else: 
        print('User not valid, please try again')
        
"""
Create a new entry on the dictionary.
The key is the user name and values the pass and the created_date.
After add the user all the dict are saved to a file
"""       
def newuser():
    USACdb = cargar_datos()
    date = datetime.date.today()
    date2 = date.strftime("%d/%m/%y")
    newuser = input ('Please ADMIN, please introduce the new user name: ')
    pwd = input ('Please introduce the password: ')
    pwd_coded = hash(pwd)
    USACdb[newuser] = [pwd_coded, date2]
    guardar_datos(USACdb)
    print('Process finished, new user added')
    
def guardar_datos(dic):
    with open("USACdb.dat", "wb") as f:
        pickle.dump(dic, f)   
    
def cargar_datos():
    try:
        with open("USACdb.dat", "rb") as f:
            return pickle.load(f)
    except (OSError, IOError) as e:
        return dict()
    
print ('Welcome to the Ultra-Secure Advanced Check ')
usuario = input ('Please introduce user name: ')
if usuario == 'admin':
    newuser()
else:
    login(usuario)
