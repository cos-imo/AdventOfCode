import sys

def main():

    file=open('input','r')                          #Ouverture du fichier d'input
    data=file.readlines()[0]

    c=0

    for i in range(0, len(data)-1):
        c+=int(data[i])*(data[i]==data[int((i+(len(data)/2))%(len(data)))])

    sys.stdout.write("The total is " + str(c))

if __name__=="__main__":
    main()