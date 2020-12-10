import sqlite3
import django
import sys
import os

from sqlite3 import Error
# from biz_test import biz_modul
from django.shortcuts import render
from django.views import generic

# from .models import Zanr, Film, Uzivatel, Clen
from django.db import models

import datetime
# from models import as_int
# from models import Zanr

#from moviebook.forms import LoginForm
#from .clen_view import ClenIndex, CurrentClenView, CreateClen, EditClen

from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, reverse
from django.contrib import messages
# from django.contrib.auth.mixins import LoginRequiredMixin

import os

from django.core.wsgi import get_wsgi_application

import csv

# from models import Prichozi_platby

from django.db import models

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhli.settings')

# application = get_wsgi_application()

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    # DB name test only
    cur = conn.cursor()
    cur.execute("PRAGMA database_list;")
    curr_table = cur.fetchall()
    for table in curr_table:
        print("skupiny - {}".format(table))

    return conn

def update_movie_clen_by_facrID(conn):
    cur = conn.cursor()
    parameter1 = "Urxova 458/8, Praha, 18600"    
    cur.execute("select Příjmení , Jméno, ČlenskéID from seznam_hracu_facr;")
    print (cur)
    rows = cur.fetchall()
    for row in rows:
        update = "update moviebook_clen set facr_id = '{2}' where prijmeni='{0}' and jmeno='{1}';".format(
            row[0], row[1], row[2])
        print("{}".format(update))
        cur.execute(update)

    try:
        cur.execute("commit;")
    except Error as e:
        print(e)

    return rows


     # print(f'Processed {line_count} lines.')



    # akce_z = Akce(nazev_akce = "Zï¿½pas Repy", datum_konani = date(2020, 10, 4).isoformat()) # Vytvorï¿½me si novï¿½ akcii
    # akce_z.save()
    # akce_z
    # Akce.objects.all()
    # akce_z = Akce.objects.get(nazev_akce="Zï¿½pas Repy")
    


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """

    cur = conn.cursor()

    cur.execute("select jmeno, prijmeni, rc from moviebook_clen")

    rows = cur.fetchall()
 #   print(rows)
    # for row in rows:
    #     update = "update moviebook_clen set facr_id = '{2}' where prijmeni='{0}' and jmeno='{1}';".format(
    #         row[0], row[1], row[2])
    #     print("{}".format(update))
    #     cur.execute(update)

    # try:
    #     cur.execute("commit;")
    # except Error as e:
    #     print(e)

    return rows



def load_vypis():
    dbcon = create_connection("../db.sqlite3")
    with open('C:\\Users\\micha\\Projects\\uhli\\Pohyby_na_uctu-2000679390_20160101-20201201.csv', encoding='UTF-8') as csv_file:
        with open('C:\\Users\\micha\\Projects\\uhli\\error_platby.csv', mode='w', encoding='UTF-8') as err_stack:
            csv_reader = csv.reader(csv_file, delimiter=';')
            err_writer = csv.writer(err_stack, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            line_count = 0
            cur = dbcon.cursor()

            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    # print(f'\t{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]}')
                    # Column names are ﻿"Datum", Objem, Měna, Protiúčet, Kód banky, Zpráva pro příjemce, Poznámka, Typ
                    try:
                        if len(row) == 8:
                            inser_str  =f"insert into moviebook_prichozi_platby (datum, objem, protiucet, kod_banky, zprava_pro_prijemce, nazev_protiuctu, typ_platby) values ('{row[0]}', {row[1]}, '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}', '{row[7]}')"
                        else: 
                            if row:
                                print ("row -- ", row)
                                err_writer.writerow(row)

                            
                        cur.execute(inser_str)
                    except Error as e:
                        print(e)
                        print("On line {0} Unexpected error: {1}".format( sys.exc_info()[0], line_count))
                        line_count += 1

                    # print(inser_str)
                    line_count += 1
                
                if line_count%100 == 0:
                    try:
                        print ("commit")
                        cur.execute("commit;")
                        # break
                    except Error as e:
                        print(e)
                        dbcon.close()
                        del dbcon     

    print ("commit")
    cur.execute("commit;")            
    dbcon.close()
    del dbcon        

def parese_payments():   
    dbcon = create_connection("../db.sqlite3")
    mc_clen = dbcon.cursor()
    platby = dbcon.cursor()
    mc_clen.execute("select jmeno, prijmeni, rc, facr_id, var_symbol from moviebook_clen")

    for row in mc_clen:
        print (f'Jmeno {row[0]}, Prijmeni {row[1]}') 
        # print (f'Jmeno {mc_clen[0]}, Prijmeni {mc_clen[1]}') 




    dbcon.close()
    del dbcon        


def update_movie_clen_kod_banky(conn):
    cur = conn.cursor()
    cur2 = conn.cursor()
    cur3 = conn.cursor()
    # parameter1 = "Urxova 458/8, Praha, 18600"    
    cur.execute("select cislo_uctu from moviebook_clen where not (cislo_uctu = 'None')")
    
    print (cur)
    rows = cur.fetchall()
    kod_banky=''
    for row in rows:
        query2=f"select kod_banky from moviebook_prichozi_platby where protiucet = '{row[0]}'"
        print ("query2", query2)
        cur2.execute(query2)
        rows2=cur2.fetchall()
        
        if len(rows2) > 0:
            print("kod banky - ",rows2[0][0])
            query3=f"update moviebook_clen set ucet_kod_banky='{rows2[0][0]}' where cislo_uctu = '{row[0]}'"
            print("query3", query3)
            cur3.execute(query3)
            cur3.execute("commit;")




def parse_platby(conn):
    c_clen = conn.cursor()
    c_platby = conn.cursor()
    # parameter1 = "Urxova 458/8, Praha, 18600"    
    queryes=[
    "select var_symbol from moviebook_clen WHERE ucet_protiucet = '{0}' and kod_banky = {1}"
    # , "select var_symbol from moviebook_clen WHERE "
    # , ""
    ]  
    c_platby.execute("select protiucet, kod_banky, zprava_pro_prijemce from moviebook_prichozi_platby;")
    # clens.execute("")
    platby_arr = c_platby.fetchall()
    # print(rows)
    new_rc = 0
    for p_ar in platby_arr:
        # print (p_ar)
        q_clen=f"select var_symbol, jmeno, prijmeni from moviebook_clen WHERE ucet_protiucet = '{p_ar[0]}' and ucet_kod_banky = '{p_ar[1]}'" 
        print(q_clen)
        c_clen.execute(q_clen)
        clen_arr = c_clen.fetchall()
        if len (clen_arr) > 0:
            q_update = f"update moviebook_prichozi_platby set facr_id='{clen_arr[0][0]}',jmeno='{clen_arr[0][1]}',prijmeni='{clen_arr[0][2]}' where protiucet = '{p_ar[0]}' and kod_banky='{p_ar[1]}' and (facr_id is null or facr_id = 1)"
            print ("q_update - ", q_update)
            c_platby.execute(q_update)
            c_platby.execute("commit")




        # platby.execute("update moviebook_prichozi_platby set")
         


        # update = "update moviebook_clen set narozen = '{0}' where id='{1}';".format(new_date, row[0])
        # print("{}".format(update))
        
        # try:
            # cur.execute(update)
            # cur.execute("commit;")
        # except Error as e:
            # print(e)

    # return rows

# dbcon=create_connection("C:\Users\micha\PycharmProjects\uhli\biz1.db")
dbcon=create_connection("../db.sqlite3")



# cur = dbcon.execute("PRAGMA database_list;")
# curr_table = cur.fetchall()
# for table in curr_table:
#   print("DB - {}".format(table))
# rows = update_movie_clen_by_facrID(dbcon)

print("stating in DB Wolk")
# update_movie_clen_kod_banky(dbcon)
parse_platby(dbcon)
dbcon.close()
del dbcon        



# ###########################
