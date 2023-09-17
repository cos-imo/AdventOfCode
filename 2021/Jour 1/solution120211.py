import sys, copy, operator, string

def main():

    file=open('input','r')
    data=[line.replace('\n','') for line in file.readlines()]

    total=0
    
    for i in range(len(data)-1):
        if data[i]<data[i+1]:
            total+=1

    sys.stdout.write("Data processed. {} value increased \n".format(total))
    

if __name__=="__main__":
    main()