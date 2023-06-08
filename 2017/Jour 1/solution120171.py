import sys

def main():

    file=open('input','r')                          #Ouverture du fichier d'input
    data=file.readlines()[0]

    c=0

    #print(lst[0])

    for i in range(0, len(data)-1):
        c+=int(data[i])*(data[i]==data[i+1])
    
    c+=int(data[0])*(data[0]==data[-1])

    sys.stdout.write("The total is " + str(c))

if __name__=="__main__":
    main()

