import sys, string

file=open('input','r')
data=[element.replace("\n","") for element in file.readlines()]

def main():

    res=[]

    for i in range(0,len(data),3):
        overlap=(set(data[i]).intersection(set(data[i+1])).intersection(set(data[i+2]))).pop()
        res.append(overlap)

    sys.stdout.write("Sum of the priorities of the item types: {}".format(sum([(string.ascii_lowercase+string.ascii_uppercase).index(element)+1 for element in res])))

if __name__=="__main__":
    main()