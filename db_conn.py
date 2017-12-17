import MySQLdb
from MySQLdb import escape_string
import time
def connection():
    conn = MySQLdb.connect(host = "localhost",
                            user = "root",
                            passwd = "root",                        db = "test")
    c = conn.cursor()
    return c, conn

def dump_in(filename):
    c, conn = connection()
    c.execute("INSERT INTO dumps (filename, creation_time) VALUES (%s, %s)",
              (escape_string(filename), int(time.time())))
    conn.commit()
    c.close()
    conn.close()
    return 1

def get_dumps():
    c, conn = connection()
    c.execute('SELECT * FROM dumps')
    results = c.fetchall()
    c.close()
    conn.close()
    return results

def dumps_links(results):
    for x in results:
        link = "/get_file/" + x[0]
        yield link