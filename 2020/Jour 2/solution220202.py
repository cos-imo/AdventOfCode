import sys, copy, operator

def main():

    file=open('input','r')
    data=[(line.replace(':','').replace('\n','').split(' ')) for line in file.readlines()]

    count=0

    for line in data:
        range=line[0].split('-')
        count+=(line[2][int(range[0])-1]==line[1])^(line[2][int(range[1])-1]==line[1])

    sys.stdout.write("Data processed. Number of correct strings: " + str(count))
    

if __name__=="__main__":
    main()