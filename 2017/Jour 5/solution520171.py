import sys

def main():

    file=open('input','r')
    data=[int(element.replace('\n','')) for element in (file.readlines())]

    current_index=0

    steps=0

    while (current_index<(len(data))):
        steps+=1
        temp=data[current_index]
        data[current_index]+=1
        current_index+=temp

    sys.stdout.write("End of calculations\nExit reached in {} steps\n".format(steps))

if __name__=="__main__":
    main()