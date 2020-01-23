'''
Created on 2020. 01. 22.
@author: ycoplusone@gmail.com
'''

import pymysql
 
conn = pymysql.connect(host='localhost', user='w2ji_eis', password='w2ji_eis',
                       db='w2ji_eis', charset='utf8')
 
try:
    # INSERT
    with conn.cursor() as curs:
        sql = "insert into customer(name,category,region) values (%s, %s, %s)"
        curs.execute(sql, ('이광수', 1, '서울'))
 
    conn.commit()
 
    # SELECT
    with conn.cursor() as curs:
        sql = "select * FROM customer"
        curs.execute(sql)
        rs = curs.fetchall()
        for row in rs:
            print(row)
 
finally:
    conn.close()