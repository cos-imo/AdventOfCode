import sys, copy, operator

def main():

    file=open('subject_input','r')
    data=[line.replace('\n','') for line in file.readlines()]

    count=0
    xposition=0
    n=len(data[0])

    for line in data[1:]:
        xposition=((xposition+3)%n)
        count+=(line[xposition]=="#")

    sys.stdout.write("Data processed. {} trees encountered".format(count))
    

if __name__=="__main__":
    main()