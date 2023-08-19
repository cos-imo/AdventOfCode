import sys, copy

def main():

    file=open('input','r')
    data=[int(element) for element in file.readlines()[0].split('\t')]

    history=[]

    n=0

    while not(data in history):
        n+=1
        history.append(copy.deepcopy(data))
        index=data.index(max(data))
        amount=max(data)
        data[index]=0
        index=(index+1)%(len(data))
        while amount:
            data[index]+=1
            index=(index+1)%(len(data))
            amount-=1

    sys.stdout.write("End of calculations.\nConfiguration achieved in {} steps.\n".format(n))

if __name__=="__main__":
    main()