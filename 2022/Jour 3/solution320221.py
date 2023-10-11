import sys, copy

file=open('input','r')
data=[element.replace("\n","") for element in file.readlines()]

def main():

    res=0

    for element in data:
        overlap=(set(element[:len(element)//2]).intersection(set(element[len(element)//2:]))).pop()
        if overlap.isupper():
            res += ord(overlap) - ord('A') + 27
        else:
            res += ord(overlap) - ord('a') + 1

    sys.stdout.write("Sum of the priorities: {}".format(res))

if __name__=="__main__":
    main()