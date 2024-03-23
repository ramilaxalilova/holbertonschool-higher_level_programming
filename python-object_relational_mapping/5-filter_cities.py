#!/usr/bin/python3
""" lists all cities from city table """
import MySQLdb
import sys


def main():
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(user=u, passwd=p, db=d, host='localhost', port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM cities c \
                LEFT JOIN states s ON c.state_id = s.id \
                ORDER BY c.id")

    [print(", ".join([state[2] for state in cur.fetchall()
     if state[4] == state_name]))]
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
