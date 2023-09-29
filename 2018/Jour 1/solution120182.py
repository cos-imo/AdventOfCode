import sys
import itertools

def main():

    file=open('input','r')
    data=[int(element) for element in file.readlines()]

    frequency=0
    history = {0}
    for element in itertools.cycle(data):
        frequency+=element
        if frequency in history:
            sys.stdout.write(str(frequency))
            break
        history.add(frequency)

if __name__=="__main__":
    main()