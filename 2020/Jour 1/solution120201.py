import sys, copy, operator

def main():

    file=open('input','r')
    data=[int(element.replace('\n','')) for element in file.readlines()]
    
    for element in data:
        popped_list=(copy.deepcopy(data))
        popped_list.pop(data.index(element))
        if (2020-element) in popped_list:
            sys.stdout.write("Number found\n{}x{}={}".format(element, 2020-element, element*(2020-element)))
            exit()

if __name__=="__main__":
    main()