from os import link
import mysql.connector as mc

link = mc.connect(
  host="localhost",
  user="root",
  password="root",
  database="vista"
)

global User_name,Row_checked, Shard_table
User_name = "Чорт"
Row_checked = None
Shard_table = ''

