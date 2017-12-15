import MySQLdb

def connection():
    conn = MySQLdb.connect(host = "localhost",
                            user = "root",
                            passwd = "test",
                            db = "test")
    c = conn.cursor()
    return c, conn