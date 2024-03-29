#!/usr/bin/python3
'''
takes in an arg and displays all values in the table
state where in db hbtn_0e_usa where name matches arg
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE\
    %(state_name)s ORDER BY id ASC", {'state_name': argv[4]})
    for row in cur.fetchall():
        if row[1] == argv[4]:
            print(row)
    db.close()
