import sys, copy

def main():

    file=open('input','r')
    lst=file.readlines()[0]

    history=[]
    coordinates=[0,0]
    counter=0

    for element in lst:
        if (coordinates not in history):
            counter+=1
            history.append(copy.deepcopy(coordinates))
        if element=='>':
            coordinates[0]+=1
        elif element=='<':
            coordinates[0]-=1
        elif element=='v':
            coordinates[1]-=1
        else:
            coordinates[1]+=1
    
    sys.stdout.write("{} households received at least one present.\n".format(counter))

if __name__=="__main__":
    main()