import hashlib
 

 
import sys

def main():

    file=open('input','r')
    string=file.readlines()[0]
    

    while (hashlib.md5(string+).digest()[0:5]!="00000"):

            
    sys.stdout.write("Total needed: " + str(res))

if __name__=="__main__":
    main()