import psycopg2
import query


def mysol(qr):
    #connect with database
    conn = psycopg2.connect("host='localhost' dbname='news' user='postgres' password= 'password'")
    c = conn.cursor()
    #QUery execution
    c.execute(qr)
    #result
    res = c.fetchall()
    print(res)
    conn.close()

def main():
    mysol(query.myfirstquery)
    mysol(query.mysecondquery)
    mysol(query.mythirdquery)

if __name__ == '__main__':
    main()
