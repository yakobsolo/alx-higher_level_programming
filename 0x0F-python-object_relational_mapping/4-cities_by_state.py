#!/usr/bin/python3
''' lists all cities from the database hbtn_0e_0_usa '''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        port=3306,
        db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
    FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY\
    cities.id ASC")
    for row in cur.fetchall():
        print(row)
    db.close()
