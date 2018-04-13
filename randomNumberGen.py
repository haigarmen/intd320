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
        # first we need to create an object for the db connection
        # the connect function needs your host, usually localhost
        # then a username
        # and password to mysql
        # finally the name of the database
        connection = mdb.connect('localhost','root','babel67','test_db');
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO randomNums(number) VALUES("%s")""" % (randomNumber))
        connection.commit()

    except mdb.Error as e:
        connection.rollback()
        print ("Error %d: %s" % (e.args[0],e.args[1]))

    connection.close()
    time.sleep(2)
