import sys, copy

def main():

    file=open('input','r')
    data=[element.replace('\n','') for element in file.readlines()]

    totals=[]
    count=0

    for line in data:
        if line=='':                #WARNING: Make sure to add an empty line at the end of input file to count the last elf :)
            totals.append(count)
            count=0
        else:
            count+=int(line)

    print(max(totals))

if __name__=="__main__":
    main()