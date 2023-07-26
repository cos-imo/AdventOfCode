import sys

def main():

    file=open('input','r')
    data=file.readlines()

    total=0

    for line in data:
        total+=((line[0]=='+')-(line[0]=='-'))*int(line[1:])

    sys.stdout.write("Total:" + str(total))

if __name__=="__main__":
    main()