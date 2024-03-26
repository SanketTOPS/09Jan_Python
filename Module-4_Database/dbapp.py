import sqlite3

try:
    dbcon=sqlite3.connect("temp.db")
    print("Database created/connected!")
except Exception as e:
    print(e)

#Table Create
create_tbl="create table studinfo(id integer primary key autoincrement,name text,sub text)"
try:
    dbcon.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)

#Insert Data
"""insert_data="insert into studinfo(name,sub)values('sanket','python'),('mitesh','java'),('hitesh','php'),('ashok','html'),('nirav','angular')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)"""

#Update Data
"""update_data="update studinfo set sub='iOS' where id=6"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""


#Delete Data
"""delete_data="delete from studinfo where name='mitesh'"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record Deleted!")
except Exception as e:
    print(e)"""

#Show Data
cr=dbcon.cursor()
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(2)
    #data=cr.fetchone()
    #print(data)

    for i in data:
        print(i)

except Exception as e:
    print(e)
    
