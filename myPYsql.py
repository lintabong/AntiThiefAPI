import pymysql


def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='redfin.id.rapidplex.com',
        user='lincodin_myroot',
        password="myguard813",
        db='lincodin_exampleDB',
    )

    cur = conn.cursor()
    cur.execute("select @@version")
    output = cur.fetchall()
    print(output)

    # To close the connection
    conn.close()

mysqlconnect()