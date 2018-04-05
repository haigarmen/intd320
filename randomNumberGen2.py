 #!/usr/bin/env python
import time
import MySQLdb as mdb
import random

def createRandomNum():
    randomNum1 = random.randint(1,500)
    randomNum2 = random.randint(1,500)
    randomNum3 = random.randint(1,500)
    print("randomNum1 = %d" %randomNum1)
    print("randomNum2 = %d" %randomNum2)
    print("randomNum3 = %d" %randomNum3)
    return randomNum1,randomNum2, randomNum3

while True:

    try:
        randomNum1, randomNum2, randomNum3 = createRandomNum()
        # first we need to create an object for the db connection
        # the connect function needs your host, usually localhost
        # then a username
        # and password to mysql
        # finally the name of the database
        connection = mdb.connect('localhost','root','babel67','test_db');
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO randomTwos(random1,random2,random3) VALUES("%s","%s","%s")""" % (randomNum1,randomNum2,randomNum3))
        connection.commit()

    except mdb.Error as e:
        connection.rollback()
        print ("Error %d: %s" % (e.args[0],e.args[1]))

    connection.close()
    time.sleep(2)
