import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    # DB name test only
    cur = conn.cursor()
    cur.execute("PRAGMA database_list;")
    curr_table = cur.fetchall()
    for table in curr_table:
        print("DB naem - {}".format(table))


    return conn

def select_all_tasks(conn, sql_text):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    #cur.execute("select UsageCode from UsageAddresList;")
    #cur.execute("PRAGMA database_list;")
    try:
        cur.execute("{}".format(sql_text))
    except Error as e:
        print(e)
    try:
        rows = cur.fetchall()
    except Error as e:
        print(e)


    # result = ""
    # for row in rows:
    #     result += "{}".format(row)
    return rows


def get_result(query):
    dbcon = create_connection("biz1.db")
    return select_all_tasks(dbcon, query)

