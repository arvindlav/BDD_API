import configparser
import mysql.connector
#from mysql.connector import Error

def getconfig():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\SESA243476\\PycharmProjects\\ParseJson\\Utilities\\properties.ini')
    return config

connection = {
    'host': getconfig()['SQL']['host'],
    'database': getconfig()['SQL']['database'],
    'user': getconfig()['SQL']['user'],
    'password': getconfig()['SQL']['password'],
}
def getPassword():
    return "vittala@1234"

def mysqlconnection():
    print((connection))
    try:
        conn = mysql.connector.connect(**connection)
        if conn.is_connected():
            print("Connection is successful")
            return conn
    except Error as e:
        print(e)

def getQuery(query):
    conn = mysqlconnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row

def addBookPayload(isbn,aisle):
    body = {
                  "name":"Learn Appium Automation with Java",
                  "isbn":isbn,
                  "aisle":aisle,
                  "author":"John foe"
            }
    return body