import sys

def main():

    file=open('input','r')                          #Ouverture du fichier d'input
    raw_data=file.readlines()

    c=0

    for i in range(0,len(raw_data)-1):
        lst = raw_data[i].split("\t")
        lst[-1]=(lst[-1][:-1])
        lst=list(map(int, lst))
        c+=(int(max(lst))-int(min(lst)))

    last=raw_data[-1].split("\t")
    last=list(map(int,last))

    c+=int(max(last)-int(min(last)))

    sys.stdout.write("The total is " + str(c))

if __name__=="__main__":
    main()