import sys, copy, operator

def main():

    file=open('input','r')
    data=file.readlines()
    data=[int(element) for element in data[0].split("-")]

    corrects=[]

    for k in range(data[0],data[1]):
        correct=1
        double=0
        for i in range((len(str(k)))-1):
            if str(k)[i+1]<str(k)[i]:
                correct=0
            if str(k)[i]==str(k)[i+1]:
                double=1
        if double and correct:
            corrects.append(k)
    print(len(corrects))

if __name__=="__main__":
    main()