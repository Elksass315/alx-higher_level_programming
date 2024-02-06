#!/usr/bin/python3
"""
script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mysql

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('Failed to connect to the database')
        exit(0)

    cursor = db.cursor()

    cuantity = cursor.execute("""SELECT c.name FROM cities as c
                      INNER JOIN states as s
                      ON c.state_id = s.id
                      WHERE s.name = '{:s}'
                      ORDER BY c.id ASC;""".format(argv[4]))

    result_query = cursor.fetchall()

    final = []

    for i in range(cuantity):
        final.append(result_query[i][0])

    print(', '.join(final))

    cursor.close()
    db.close()
