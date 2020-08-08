#!/usr/bin/python3
"""
lists all cities from the database in ascending order
with state name using MySQLdb
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name FROM cities AS c \
                INNER JOIN states AS s ON c.state_id = s.id \
                ORDER BY c.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
