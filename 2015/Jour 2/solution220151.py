import sys

def main():

    file=open('input','r')
    lst=file.readlines()

    res=0

    for line in lst:
        lst=[int(x) for x in line.split("x")]
        res+=2*(lst[0]*(lst[1]+lst[2]) + lst[1]*lst[2]) + min([lst[0]*lst[1],lst[0]*lst[2],lst[1]*lst[2]])
            
    sys.stdout.write("Total needed: " + str(res))

if __name__=="__main__":
    main()