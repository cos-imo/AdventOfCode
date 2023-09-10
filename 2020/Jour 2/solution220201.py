import sys, copy, operator

def main():

    file=open('input','r')
    data=[(line.replace(':','').replace('\n','').split(' ')) for line in file.readlines()]

    count=0

    for line in data:
        range=line[0].split('-')
        if (int(range[0])<=line[2].count(line[1])) and (line[2].count(line[1])<=int(range[1])):
            count+=1

    print(count)
    

if __name__=="__main__":
    main()