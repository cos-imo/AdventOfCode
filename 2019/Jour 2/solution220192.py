import sys, copy

def main():

    file=open('input','r')
    original_data=(file.readlines()[0]).split(',')

    res=0
    target=19690720

    for k in range(0,99):
        for j in range(0,99):
            data=copy.deepcopy(original_data)
            data[1]=k
            data[2]=j
            if res==target:
                sys.stdout.write("solution processed. \nnoun: " + str(data[1]) + "\nverb: " + str(data[2]-1) + "\nfinal output: " + str(100*int(data[1])+int(data[2]-1)) + "\n\n")
                return
            else:
                for i in range (0,len(data),4):
                    if data[i]=='1':
                        data[int(data[i+3])]=int(data[int(data[i+1])])+int(data[int(data[i+2])])
                    elif data[i]=='2':
                        data[int(data[i+3])]=int(data[int(data[i+1])])*int(data[int(data[i+2])])
                    elif data[i]=='99':
                        sys.stdout.write("program exited gracefully.\nreturned value: " + str(data[0])+"\n")
                        res=data[0]

if __name__=="__main__":
    main()