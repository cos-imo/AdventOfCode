import sys

def main():

    file=open('input','r')
    lst=file.readlines()

    res=0

    for line in lst:
        lst=[int(x) for x in line.split("x")]
        product=1
        for element in lst:
            product*=element
        res+=2*min(lst)
        lst.pop(lst.index(min(lst)))
        res+=2*min(lst)+product
            
    sys.stdout.write("Total ribbon length needed: " + str(res))

if __name__=="__main__":
    main()