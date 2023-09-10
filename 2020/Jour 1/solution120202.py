import sys, copy, operator

def main():

    file=open('input','r')
    data=[int(element.replace('\n','')) for element in file.readlines()]

    # It's 1AM over here so I was too lazy to think n decided to just just bruteforced it

    for i in range(len(data)-2):
        for j in range(i+1,len(data)):
            for k in range(j+1,len(data)):
                if data[i]+data[j]+data[k]==2020:
                    sys.stdout.write("Solution found\n{}x{}x{}={}".format(data[i], data[j], data[k],data[i]*data[j]*data[k]))
    

if __name__=="__main__":
    main()