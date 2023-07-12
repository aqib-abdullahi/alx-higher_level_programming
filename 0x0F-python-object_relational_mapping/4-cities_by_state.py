#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Access to the database and get the cities
    from the database.
    """
    if len(sys.argv) >= 4:
        db_connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        cursor = db_connection.cursor()
        cursor.execute(
            'SELECT cities.id, cities.name, states.name FROM cities' +
            ' INNER JOIN states ON cities.state_id = states.id' +
            ' ORDER BY cities.id ASC;'
        )
        results = cursor.fetchall()
        for result in results:
            print(result)
        db_connection.close()
