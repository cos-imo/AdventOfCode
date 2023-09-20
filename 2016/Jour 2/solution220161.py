import sys, copy

def main():

    file=open('input','r')
    data=file.readlines()

    coordinates=[1,1]
    positions=[]

    code=[[7,8,9],[4,5,6],[1,2,3]]

    for line in data:
        for element in line:
            if element=="U":
                if coordinates[1]<2:
                    coordinates[1]+=1
            elif element=="D":
                if coordinates[1]>0:
                    coordinates[1]-=1
            elif element=="L":
                if coordinates[0]>0:
                    coordinates[0]-=1
            elif element=="R":
                if coordinates[0]<2:
                    coordinates[0]+=1
            elif element=="\n":                                     #WARNING: be sure to add a blank line at the end fo the file or you might miss a digit!
                positions.append(copy.deepcopy(coordinates))
            else:
                print("Error: Unknown symbol encountered")

    sys.stdout.write("The code is: ")
    for element in positions:
        sys.stdout.write(str(code[element[1]][element[0]]))

if __name__=="__main__":
    main()