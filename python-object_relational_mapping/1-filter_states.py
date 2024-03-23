#!/usr/bin/python3
""" lists all states with a name starting with N (upper N) """
import MySQLdb
import sys


def main():
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    db = MySQLdb.connect(user=u, passwd=p, db=d, host='localhost', port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")

    [print(state) for state in cur.fetchall() if state[1][0] == 'N']
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
