import sys

def main():

    file=open('input','r')
    data=(file.readlines()[0]).split(',')

    for i in range (0,len(data),4):
        if data[i]=='1':
            data[int(data[i+3])]=int(data[int(data[i+1])])+int(data[int(data[i+2])])
        elif data[i]=='2':
            data[int(data[i+3])]=int(data[int(data[i+1])])*int(data[int(data[i+2])])
        elif data[i]=='99':
            sys.stdout.write("program exited gracefully.\nreturned value: " + str(data[0]))
            return
        else:
            sys.stdout.write(str(i) + " instruction: " + str(data[i]) + " " + ":error encountered\n")
            return

if __name__=="__main__":
    main()