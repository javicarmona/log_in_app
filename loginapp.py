#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 00:51:19 2019

@author: javiercarmona
"""

import datetime
import pickle #pickle is a module to save .dat files

"""
Log in open de dictionary from the dat file.
Check if the user name is on the database and ask for password.
"""
def login(uname):
    USACdb = cargar_datos()
    if uname in USACdb:
        passwordx = hash(input ('Welcome, please introduce password: '))
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
    pwd_coded = hash(input ('Please introduce the password: '))
    USACdb[newuser] = [pwd_coded, date2]
    guardar_datos(USACdb)
    print('Process finished, new user added')
    
def newuser():
    USACdb = cargar_datos()
    date = datetime.date.today()
    date2 = date.strftime("%d/%m/%y")
    newuser = input ('Please ADMIN, please introduce the new user name: ')
    pwd_coded = hash(input ('Please introduce the password: '))
    USACdb[newuser] = [pwd_coded, date2]
    guardar_datos(USACdb)
    print ("")
    print('Process finished, new user added')
    input('Press any key to continue')

    
def guardar_datos(dic):
    with open("USACdb.dat", "wb") as f:
        pickle.dump(dic, f)   
    
def cargar_datos():
    try:
        with open("USACdb.dat", "rb") as f:
            return pickle.load(f)
    except (OSError, IOError) as e:
        return dict()

def remove_user():
    USACdb = cargar_datos()
    print ('List of active users on USAC:')
    print(USACdb.keys())
    print ('-----------------------------')
    for i in USACdb:
        print (i)
    reg_del = input ('Please introduce the user to DELETE: ')
    if reg_del in USACdb:
        del USACdb[reg_del]
        print('')
        print ('The user ', reg_del, 'was been deleted, have a nice day' )
        input('Press any key to continue')
    else:
        print ('Unable to find ', reg_del, 'on our database' )
    guardar_datos(USACdb)

def check_users():
    print ("Exporting active users in Ultra-Secure Advanced Check ")
    USACdb = cargar_datos()
    for i in USACdb:
        print ("\t>> User: ", i, '       Created date: ',USACdb[i][1])
    print ("")
    input ('Press any key to continue...')
    print ("")

    
def admin_menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    print ("")
    print ("Welcome ADMIN, this is what you can do")
    print ("\t1 - Add new user")
    print ("\t2 - Remove user")
    print ("\t3 - Check active users")

    
    # solicituamos una opción al usuario
    opcionMenu = input("Introduce a number >> ")
 
    if opcionMenu=="1":
        print ("")
        newuser()
    elif opcionMenu=="2":
        print ("")
        remove_user()
    elif opcionMenu=="3":
        print ("")
        check_users()
    else:
        print ("")
        input("No valid option, thank you!")
        print ("")
        
def main():
    while True: 
        print (" ")
        print ('Welcome to the Ultra-Secure Advanced Check ')
        print ('Choose an option: ')
        print ("\t1 - Log in")
        print ("\t2 - Exit")
        opcionMenu = input("Introduce a number >> ")
        if opcionMenu=="1":
            print ("")
            usuario = input ('Please introduce user name: ')
            if usuario == 'admin':
                admincode = 'canela'
                pwd = input ('Please introduce admin the password: ')
                print ("")
                if pwd == admincode:
                    admin_menu()
                else: 
                    pass
            else:
                login(usuario)
    
        elif opcionMenu=="2":
            print ("")
            print ('Thank you for use Ultra-Secure Advanced Check, bye bye! ')
            break
        else:
            print ("")
            input("Option not valid.")
            
main()
    