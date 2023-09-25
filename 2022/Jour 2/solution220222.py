import sys

def main():

    file=open('input','r')
    lst=[element.replace('\n','').replace(' ','') for element in file.readlines()]

    score=0

    combinations = ["AY","AZ","AX","BX","BY","BZ","CZ","CX","CY"]
    player=['X','Y','Z']

    for line in lst:
        score+=player.index(line[1])*3+1+(combinations.index(line)%3)

    sys.stdout.write("Total score: {}\n".format(score))

if __name__=="__main__":
    main()
