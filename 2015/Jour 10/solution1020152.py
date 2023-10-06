import sys, copy
from itertools import *

def main():

    file=open('input','r')
    data=file.readlines()

    instruction=data[0]

    for i in range(50):
        counter=1
        string=''
        for i in range(0,len(instruction)-1):
            if instruction[i]==instruction[i+1]:
                counter+=1
            else:
                string+=str(counter)+instruction[i]
                counter=1
        string+=str(counter)+instruction[-1]
        instruction = copy.deepcopy(string)

    sys.stdout.write("The length of the result after 40 iterations is " + str(len(string)))


if __name__=="__main__":
    main()