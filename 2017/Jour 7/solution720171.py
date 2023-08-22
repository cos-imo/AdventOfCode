import sys, copy

def main():

    file=open('input','r')
    data=[element.replace('(','').replace(')','').replace('\n','').replace(',','').split(' ') for element in file.readlines()]

    children=set([])
    nodes=set([])

    for list in data:
        if len(list)>=3:
            for element in list[3:]:
                children.add(element)
        nodes.add(list[0])

    for element in nodes:
        if not (element in children):
            sys.stdout.write("End of computations.\nThe bottom program is named {}.\n".format(element))

if __name__=="__main__":
    main()