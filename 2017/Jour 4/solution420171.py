import sys, copy

def main():

    file=open('input','r')
    data=file.readlines()

    total=0

    for line in data:
        res=1
        lst=line.split(' ')
        for i in range(0,len(lst)):
            if (lst[i] in (lst[:i]+lst[(i+1):])) or (str(lst[i]+"\n") in (lst[:i]+lst[(i+1):])):
                res=0
        total+=res
    sys.stdout.write("Total strings: " + str(total))

if __name__=="__main__":
    main()