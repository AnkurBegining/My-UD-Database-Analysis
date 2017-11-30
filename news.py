#!/usr/bin/env python3.6

import psycopg2
import query


def mysol(qr, str):
    #connect with database
    conn = psycopg2.connect("host='localhost' dbname='news' user='postgres' password= 'password'")
    c = conn.cursor()
    #QUery execution
    c.execute(qr)
    #result
    res = c.fetchall()

    if str == 'first':
        print("\nWhat are the top three articles of all time?\n")
        for title, views in res:
            print("    {}  -  {} views".format(title, views))
    elif str == 'second':
        print("\nWho are the most popular article authors of all time?\n")
        for title, views in res:
            print("    {}  -  {} views".format(title, views))
    else:
        print("\nOn which days did more than 1% of requests lead to errors?\n")
        for da, err in res:
            print("    {}  -  {} error".format(da, err))


    conn.close()

def main():
    mysol(query.myfirstquery, 'first')
    mysol(query.mysecondquery, 'second')
    mysol(query.mythirdquery, 'third')

if __name__ == '__main__':
    main()
