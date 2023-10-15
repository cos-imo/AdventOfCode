import sys, copy, operator

def main():

    file=open('subject_input','r')
    data=[line.replace('\n','') for line in file.readlines()]

    print(data)
    

if __name__=="__main__":
    main()