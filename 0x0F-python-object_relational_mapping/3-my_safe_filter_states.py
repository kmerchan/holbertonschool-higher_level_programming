#!/usr/bin/python3
"""
lists all states from the database in ascending order
where name of state matches argument given using MySQLdb
"""
if __name__ == "__main__":
    import argv from sys
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT id, name FROM state WHERE name=argv[4]
                ORDER BY states.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
