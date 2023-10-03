import sys, string ,difflib, copy

def main():

    file=open('input','r')
    data=file.readlines()
    
    res=[]

    for line in data:
        for letter in line:
            for element in data[data.index(line)+1:]:
                if (line[:(line.index(letter))]+line[(line.index(letter))+1:])==(element[:(line.index(letter))]+element[(line.index(letter))+1:]):
                    res.append(line[:(line.index(letter))]+line[(line.index(letter))+1:])

    sys.stdout.write("The common letters between the two correct box IDs are {} \n".format(res[0]))

if __name__=="__main__":
    main()