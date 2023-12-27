import sys, copy

def main():

    file=open('input','r')
    data=[element.replace('\n','') for element in file.readlines()]
    res=[]

    for line in data:
        line=[element for element in line if element.isdigit()]
        res.append(int(str(line[0])+str(line[-1])))

    sys.stdout.write("The sum of the calibration values is " + str(sum(res)) + ".\n")

if __name__=="__main__":
    main()
