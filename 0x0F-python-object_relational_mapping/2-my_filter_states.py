#!/usr/bin/python3
''' lists all states from the database hbtn_0e_0_usa '''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        port=3306,
        db=argv[3],
        state_name=argv[4])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE\
    '{:s}' ORDER BY id ASC".format(state_name)
    for row in cur.fetchall():
        print(row)
    db.close()
