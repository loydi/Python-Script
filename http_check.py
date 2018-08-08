#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import requests,argparse,urllib3

urllib3.disable_warnings()
def check(arg1):
    r = requests.get(arg1)
    
    if r.status_code ==200:
        print ('System is OK.. : OK')
        exit (0)
    else:
        print ('Can not access site')
        exit (2)

def main(): 
    #Argüman tanımlama
    parser = argparse.ArgumentParser()
    parser.add_argument("--url","-u",help="Site Url")
    veri = parser.parse_args()
    check(veri.url)
if __name__ == '__main__':
    main()