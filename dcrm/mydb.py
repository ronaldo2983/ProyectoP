# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost", 
    user = "root",
    passwd = "Rjrj83rj",
)

# prepare a cursor object
cursorobj = dataBase.cursor()

# create a database
cursorobj.execute("CREATE DATABASE ProyectoP")

print ("All Done!")