import sys, copy, operator, string

def main():

    file=open('input','r')
    data=[line.replace('\n','') for line in file.readlines()]

    bits_counter=[0 for i in range(len(data[0]))]
    gamma_rate=''
    epsilon_rate=''

    for entry in data:
        for i in range(len(entry)):
            if entry[i]=="1":
                bits_counter[i]+=1

    for i in range(len(bits_counter)):
        gamma_rate+=str(int(bits_counter[i]>(len(data)/2)))

    for element in gamma_rate:
        epsilon_rate+=str(1-int(element))
    
    sys.stdout.write("Data processed.\n \t\tGamma rate: {}\n\t\tEpsilon rate: {}\n\tSorry but I couldn't find out how to convert to integer easily so I gave up. Compute it yourself \n".format(gamma_rate, epsilon_rate))
    

if __name__=="__main__":
    main()