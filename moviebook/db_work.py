import sqlite3
import django
django.setup()


from sqlite3 import Error
from biz_test import biz_modul
from django.shortcuts import render
from django.views import generic

#from .models import Zanr, Film, Uzivatel, Clen
#from moviebook.forms import LoginForm
#from .clen_view import ClenIndex, CurrentClenView, CreateClen, EditClen

from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


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

    #DB name test only
    cur = conn.cursor()
    cur.execute("PRAGMA database_list;")
    curr_table = cur.fetchall()
    for table in curr_table:
        print("skupiny - {}".format(table))

    return conn

def update_movie_clen_by_facrID(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """

    cur = conn.cursor()
    parameter1 = "Urxova 458/8, Praha, 18600"
#     cur.execute("select com.CompanyIN, EmployeeLowerBound, ActivityScore, IsHq, AddressText, NaceCode, Nace, NaceSection, NaceSectionCode, FlatCount, UsageLabel, UsageCode  from Company com, AddressCompany acom, AddressBuilding abuild,  AdresniMisto am \
# where \
# com.CompanyIN = acom.CompanyIN AND \
# abuild.AddressCode = acom.AddressCode AND \
# am.Kod = abuild.AddressCode \
# and abuild.AddressText = '{}' \
# ".format(parameter1))

    cur.execute("select Příjmení , Jméno, ČlenskéID from seznam_hracu_facr;")
                # "select moviebook_clen.jmeno, moviebook_clen.prijmeni,  from moviebook_clen;")

    #cur.execute("insert into groups values (1 , 'skupina 1')")
    #cur.execute("select * from groups")
    #cur.execute("CREATE TABLE groups (group_id INTEGER PRIMARY KEY,name TEXT NOT NULL);")

    rows = cur.fetchall()
 #   print(rows)
    for row in rows:
        update = "update moviebook_clen set facr_id = '{2}' where prijmeni='{0}' and jmeno='{1}';".format(row[0], row[1], row[2])
        print("{}".format(update))
        cur.execute(update)

    try:
        cur.execute("commit;")
    except Error as e:
        print(e)

    return rows

def GetPlatbyAll(conn):
    cur = conn.cursor()




#u


#dbcon=create_connection("C:\Users\micha\PycharmProjects\uhli\biz1.db")

dbcon=create_connection("../db.sqlite3")
# cur = dbcon.execute("PRAGMA database_list;")
# curr_table = cur.fetchall()
# for table in curr_table:
#     print("DB - {}".format(table))

# rows = update_movie_clen_by_facrID(dbcon)
# print(rows)


#print(usage_list)

rows = select_all_tasks(dbcon)

for row in rows:
    for field in row:
        print("{}".format(field))

# ###########################
