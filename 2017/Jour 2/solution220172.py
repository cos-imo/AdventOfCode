import sys

def main():

    file=open('input','r')                          #Ouverture du fichier d'input
    raw_data=file.readlines()

    c=0

    for i in range(0,len(raw_data)-1):
        lst = raw_data[i].split("\t")
        lst[-1]=(lst[-1][:-1])
        lst=list(map(int, lst))
        for k in range(0, len(lst)-1):
            for j in range(k+1, len(lst)):
                c+=(lst[k]/lst[j])*((lst[k]/lst[j])==(lst[k]//lst[j]))

    last=raw_data[-1].split("\t")
    last=list(map(int,last))
    for i in range(0, len(last)-1):
        for j in range(i+1, len(lst)):
            c+=(i/j)*((i/j)==(i//j))

    sys.stdout.write("The total is " + str(c))

if __name__=="__main__":
    main()