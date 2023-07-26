import sys, string

def main():

    file=open('input','r')
    data=file.readlines()
    alphabet=string.ascii_lowercase

    double=0
    triple=0

    for line in data:
        counter=[0 for i in range(26)]
        for letter in line[:-1]:
            counter[alphabet.index(letter)]+=1
        if counter.count(2):
            double+=1
        if counter.count(3):
            triple+=1

    sys.stdout.write("Checksum:" + str(double*triple)+"\n")

if __name__=="__main__":
    main()