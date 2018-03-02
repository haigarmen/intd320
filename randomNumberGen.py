#!/usr/bin/env python
import time
import MySQLdb as mdb
import random

def createRandomNum():
    randomNum = random.randint(1,500)
    print("randomNumber = %d" %randomNum)
    return randomNum

while True:

    try:
        randomNumber = createRandomNum()
        connection = mdb.connect('localhost','root','','test_db');
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO randomNums(number) VALUES("%s")""" % (randomNumber))
        connection.commit()

    except mdb.Error as e:
        connection.rollback()
        print ("Error %d: %s" % (e.args[0],e.args[1]))

    connection.close()
    time.sleep(10)
 
