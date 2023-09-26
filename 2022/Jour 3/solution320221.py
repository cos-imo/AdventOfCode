import sys, copy

file=open('subject_input','r')
data=[element.replace("\n","") for element in file.readlines()]

def main():

    res=0
    acc=[]

    for element in data:
        for letter in element[:(int((len(element)/2)))]:
            if letter in element[(int((len(element)/2))):] and letter not in acc:
                res+=ord(letter)-96*(letter==letter.lower())-38*(letter==letter.upper())
                acc.append(letter)

    sys.stdout.write("Sum of the priorities: {}".format(res))

if __name__=="__main__":
    main()