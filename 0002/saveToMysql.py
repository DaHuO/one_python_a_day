# -*- coding: UTF-8 -*-

import MySQLdb


def saveToMysql():
    file_in = open('activation_code', 'r')
    db = MySQLdb.connect(host = "localhost",
                         user = "",
                         passwd = "",
                         db = "")
    table_name = "test"
    cur = db.cursor()
    count = 0
    for line in file_in:
        stmt = "insert into " + table_name + " values(" + str(count) + ",'" + \
            line + "');"
        cur.execute(stmt)
        count += 1
    db.close()
    file_in.close()

if __name__ == "__main__":
    saveToMysql()
