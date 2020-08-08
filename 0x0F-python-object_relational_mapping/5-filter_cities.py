#!/usr/bin/python3
"""
lists all cities from the database in ascending order
matching state name passed in as argument using MySQLdb
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT c.name FROM cities AS c \
                INNER JOIN states AS s ON c.state_id = s.id\
                WHERE s.name = '{}' \
                ORDER BY c.id ASC""".format(argv[4]))
    rows = cur.fetchall()
    for i, row in enumerate(rows, start=0):
        if i != 0:
            print(", ", end="")
        print(row[0], end="")
    print("")
    cur.close()
    db.close()
