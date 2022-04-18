from array import array
from dataclasses import fields
import datetime
# import mysql.connector
from config import link as linkdb 
from config import linktel as linktel
import mysql.connector as mc
import dategen


def getall_recs(table):
  mycursor = linkdb.cursor()
  mycursor.execute(f"SELECT * FROM {table}")
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

def getcol_recs(col,table):
  mycursor = linktel.cursor()
  mycursor.execute(f"SELECT {col} FROM {table}")
  myresult = mycursor.fetchall()
  return myresult
  # for x in myresult:
  #   print(x[0]+x[1])
    
# внесение новой записей
def put_rec(fields,val_fields,table):
  mycursor = linkdb.cursor()
  sql = f"INSERT INTO {table} ({fields}) VALUES (%s, %s, %s)"
  print(sql)
  mycursor.execute(sql, val_fields)
  linkdb.commit()
  print(mycursor.rowcount, "записей внесено.")

# нахождение записи
def find_recs(table,filter):
  mycursor = linkdb.cursor()
  print(filter)
  sql = f"SELECT * FROM {table} WHERE {filter}"
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)  
  mycursor.close
  

# удаление записи
def del_recs(filter,table):
  mycursor = linkdb.cursor()
  sql = "DELETE FROM {table} WHERE {filter}"
  mycursor.execute(sql)
  linkdb.commit()
  print(mycursor.rowcount, "записей удалено")

# изменение записи
def update_rec(table,filter,update_str):
  mycursor = linkdb.cursor()
  sql = "UPDATE {table} SET {update_str} WHERE {filter}"
  mycursor.execute(sql)
  linkdb.commit()
  print(mycursor.rowcount, "записей обновлено")


fields = "first_name, last_name"
names = getcol_recs(fields,"name_list")
fields_vista = "username,tel,birth"
for x in names:
    tel_user,birth_user = dategen.gen_tel_birth("1/1/1993 1:30 PM", "1/1/2009 4:50 AM")
    
    print(x[0]+x[1]+' '+tel_user+' '+birth_user)
    val_fields = [x[0].lstrip()+x[1],tel_user,birth_user]
    put_rec(fields_vista,val_fields,'tel_dict')

# fields = "username, tel, birth"
# now = datetime.date(2009, 5, 5).strftime('%Y-%m-%d')
# val_fields = ("Сидоров Сидор Сидорович", "+7(911)444-33-22", now )
# print(val_fields)
# getall_recs("tel_dict")

# letters = "пи"
# print(type(letters))
# shard = "username REGEXP "+ "'^("+"|".join(letters)+")'"
# find_recs("tel_dict",shard)
# put_rec(fields,val_fields,"tel_dict")
# find_recs('first_name = "Николаева"',"name_list")
# обработка кнопки вход

