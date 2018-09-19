#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import requests,argparse,urllib3
import MySQLdb

urllib3.disable_warnings()

def mysql_ex(host,db,user,passwd,sorgu):
  
    try:
        db = MySQLdb.connect(host=host,db=db,user=user,passwd=passwd)
        cursor = db.cursor()
        cursor.execute(sorgu)
        data = cursor.fetchone()
        if (data[0] == 0):
            print("Kayıt Sayısı: %s " % data)
            exit (0)
        else:
            print("Kayıt Sayısı: %s " % data)
            exit (1)
        db.close()
    except MySQLdb.OperationalError:
        print("Argüman girişlerinde hata vardır... Kontrol Ediniz")

    
    

def main():
    
    #Argüman tanımlama
    parser = argparse.ArgumentParser()
    parser.add_argument("-H",help="Hostname veya ip adresi")
    parser.add_argument("-d",help="db name")
    parser.add_argument("-u",help="user")
    parser.add_argument("-p",help="Password")
    parser.add_argument("-q",help="""sql query -- '-q "selectcount(1)"'""")
    veri = parser.parse_args()
    
    if veri.H and veri.d and veri.u and veri.p and veri.q:
        
	    mysql_ex(veri.H,veri.d,veri.u,veri.p,veri.q)
    else:
        print("Eksik veri girisi tüm parametreleri doldurunuz")

if __name__ == '__main__':
    main()
    