#!/usr/bin/python3
""" lists all states with a name starting with N (upper N)"""

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
    
    select = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(argv[4])
    cursor.execute(select)

    result_query = cursor.fetchall()

    for row in result_query:
        print(row)

    cursor.close()
    db.close()
