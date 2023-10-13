import sys, copy, numpy

def main():

    file=open('input','r')
    data=[line.replace('\n','') for line in file.readlines()]

    shiftlist=[(1,1),(3,1),(5,1),(7,1),(1,2)]
    res=[]

    for shift in shiftlist:
        count=0
        xposition=0
        for i in range(0, len(data), shift[1]):
            count+=(data[i][xposition]=="#")
            xposition=((xposition+shift[0])%len(data[0]))
        res.append(count)

    sys.stdout.write("Product of the number of trees encountered on each of the listed slopes: {} ".format(numpy.prod(res)))
    

if __name__=="__main__":
    main()