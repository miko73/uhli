# %matplotlib inline
import numpy as np
import pandas as pd
import matplotlib
import sqlite3

print(pd)

# pd.test()


df = pd.read_csv("C:\\Users\\micha\\Projects\\uhli\\Pohyby_na_uctu-2000679390_20160101-20201204.csv", sep=";")
print ("len df - ", len(df))
print("df size - ", df.size)
print(df.head())
print(df.tail())
print(df.columns)



# print(df.sort_values((['Datum']))[['Datum', 'Objem', 'Zpráva pro příjemce']][:10])
z_uctu=df['Protiúčet'].value_counts().head(20)
print("pocty plateb z uctu -", z_uctu)
# z_uctu.plot(kind='bar')
dbcon = create_connection("C:\\Users\\micha\\Projects\\uhli\\db.sqlite3")
cur = dbcon.cursor()
cur.execute("select * from moviebook_clen")
for row in cur:
    print (f'Jmeno {row[1]}, Prijmeni {row[2]}') 
        # print (f'Jmeno {mc_clen[0]}, Prijmeni {mc_clen[1]}') 
dbcon.close()
del dbcon       



