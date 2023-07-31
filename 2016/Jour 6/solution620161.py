import sys, copy, string

def main():

    file=open('input','r')
    raw_data=[element.replace("\n","") for element in file.readlines()]
    alphabet=string.ascii_lowercase

    frequencies=[[0 for i in range(len(alphabet))] for j in range(len(raw_data[0]))]

    for i in range(len(raw_data[0])):
        for line in raw_data:
            frequencies[i][alphabet.index(line[i])]+=1

    res="".join([alphabet[list.index(max(list))] for list in frequencies])
        
    sys.stdout.write("\n\t=> The corrected message is: {} \n\n".format(res))


if __name__=="__main__":
    main()