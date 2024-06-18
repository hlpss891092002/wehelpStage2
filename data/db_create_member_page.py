import mysql.connector
import json

def connection():
  try:
    dbconfig = {
        "host":"localhost",
        "user":"root",
        "password":"00000000",
        "database":"wehelp_stage2_taipei_spot",
    }
    cnxpool = mysql.connector.pooling.MySQLConnectionPool(
      pool_name="mypool",
      pool_size=32,
      **dbconfig
    )
    cnx1 = cnxpool.get_connection()
    return cnx1
  except:
    print("db connection fail")

def createMemberTable():
  con = connection()
  cursor = con.cursor(dictionary = True)
  try:
    sql = """CREATE TABLE member_table(
    id BIGINT AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    email varchar(1000) NOT NULL,
    password varchar(255) NOT NULL,
    primary key(id)
    )"""
    cursor.execute(sql,)
    print("create table member_table")
  except:
    print("fail")
  finally:
    con.close()
    cursor.close()
  pass

createMemberTable()