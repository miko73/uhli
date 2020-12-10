import sqlite3
from sqlite3 import Error
# from biz_modul import biz_test
import pandas as pd
import matplotlib.pyplot as plt
import sys


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    # conn = None
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


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    # cur = conn.cursor()
    # cur.execute("select UsageCode, UsageLabel from UsageAddresList")
    #

    parameter1 = "Urxova 458/8, Praha, 18600"
#     cur.execute("select com.CompanyIN, EmployeeLowerBound, ActivityScore, IsHq, AddressText, NaceCode, Nace, NaceSection, NaceSectionCode, FlatCount, UsageLabel, UsageCode  from Company com, AddressCompany acom, AddressBuilding abuild,  AdresniMisto am \
# where \
# com.CompanyIN = acom.CompanyIN AND \
# abuild.AddressCode = acom.AddressCode AND \
# am.Kod = abuild.AddressCode \
# and abuild.AddressText = '{}' \
# ".format(parameter1))

    #cur.execute("insert into groups values (1 , 'skupina 1')")
    #cur.execute("select * from groups")
    #cur.execute("CREATE TABLE groups (group_id INTEGER PRIMARY KEY,name TEXT NOT NULL);")

    rows = cur.fetchall()
#    print(rows)
#     for row in rows:
#         print("skupiny - {}".format(row))

    return rows

#usage_list = biz_modul.get_result("select UsageCode, UsageLabel from UsageAddresList;")
# print(usage_list)


con = create_connection("../biz1.db")
# Read sqlite query results into a pandas DataFrame

pd.TEST_CHARSET: {'charset': 'iso-8859-1', 'use_unicode': True, }

df = pd.read_sql_query("select pocet_firem, AddressText, AddressCode, emp_num, FlatC from \
( \
select count(*) pocet_firem, abuild.AddressText, abuild.AddressCode, max( cast(com.EmployeeLowerBound AS INTEGER) * IsHq) emp_num, max(FlatCount) FlatC \
from Company com, AddressCompany acom, AddressBuilding abuild,  AdresniMisto am  \
where  \
com.CompanyIN = acom.CompanyIN AND \
abuild.AddressCode = acom.AddressCode AND \
am.Kod = abuild.AddressCode \
and IsHq=1                      \
and not UsageCode in (1, 3, 6, 7)           \
GROUP by abuild.AddressText, abuild.AddressCode  \
)  \
order by pocet_firem DESC;", con)

# Verify that result of SQL query is stored in the dataframe

# print(df)
# for row in df.iterrows():
#     print (row)

#print(df['UsageCode'],df['UsageLabel'] )
#print(df[['UsageCode','UsageLabel']] )
# encoding = "UTF-8"
# con.text_factory = lambda x: str(x, encoding)

# source = str(source, "utf8")
print(df[0:-1])
# where FlatC < 10


#print(df.query('FlatC < "10" '))


# dbcon=create_connection("C:\Users\micha\PycharmProjects\uhli\biz1.db")
# dbcon=create_connection("../biz1.db")
# rows = select_all_tasks(dbcon)
# for row in rows:
#     for field in row:
#         print("{}".format(field))
