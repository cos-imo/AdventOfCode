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

    top_three=0

    for i in range(3):
        top_three+=max(totals)
        totals.pop(totals.index(max(totals)))

    sys.stdout.write("{} calories caried by those elves.".format(top_three))

if __name__=="__main__":
    main()