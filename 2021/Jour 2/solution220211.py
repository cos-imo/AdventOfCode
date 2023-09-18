import sys, copy, operator, string

def main():

    file=open('input','r')
    data=[line.replace('\n','') for line in file.readlines()]

    total=0

    position=[0,0]

    aim=0

    for entry in data:
        entry=entry.split(' ')
        if entry[0]=="forward":
            position[0]+=int(entry[1])
            position[1]+=(aim*int(entry[1]))
        elif entry[0]=="up":
            aim-=int(entry[1])
        else:
            aim+=int(entry[1])

    sys.stdout.write("Data processed.\n \t\tX position: {}\n\t\tY position: {}\n\t Result:{} \n".format(position[0],position[1],position[0]*position[1]))
    

if __name__=="__main__":
    main()