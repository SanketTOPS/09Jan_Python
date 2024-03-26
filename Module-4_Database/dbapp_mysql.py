import pymysql

try:
    dbcon=pymysql.connect(host='127.0.0.1',user='root',password='',database='hellodb')
    print("Database Connected!")
except Exception as e:
    print(e)


cr=dbcon.cursor()
#Table Create
create_tbl="create table studinfo(id integer primary key auto_increment,name text,sub text)"
try:
    cr.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)


#Insert Data
"""insert_data="insert into studinfo(name,sub)values('sanket','python'),('mitesh','java'),('hitesh','php'),('ashok','html'),('nirav','angular')"
try:
    cr.execute(insert_data)
    dbcon.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)"""


#Update Data
"""update_data="update studinfo set sub='iOS' where id=1"
try:
    cr.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

#Delete Data
"""delete_data="delete from studinfo where name='mitesh'"
try:
    cr.execute(delete_data)
    dbcon.commit()
    print("Record Deleted!")
except Exception as e:
    print(e)"""

#Show Data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    #data=cr.fetchall()
    #data=cr.fetchmany(2)
    data=cr.fetchone()
    print(data)

except Exception as e:
    print(e)
    