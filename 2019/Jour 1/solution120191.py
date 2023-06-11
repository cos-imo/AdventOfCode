import sys

def main():

    file=open('input','r')
    lst=file.readlines()

    res=[]

    for line in lst:
        res.append(int(int(line)/3)-2)
    
    sys.stdout.write("total: " + str(sum(res)))

if __name__=="__main__":
    main()