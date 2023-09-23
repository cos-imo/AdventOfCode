import sys, re

def main():

    file=open('input','r')
    lst=[element.replace('\n','') for element in file.readlines()]

    grid=[[0 for i in range(1000)] for j in range(1000)]

    res=0

    for line in lst:
        temp = re.findall(r'\d+', line)
        for i in range(int(temp[0]), int(temp[2])+1):
            for j in range(int(temp[1]), int(temp[3])+1):
                if ("turn off" in line[:line.index(temp[0])]):
                    grid[i][j]=max(grid[i][j]-1, 0)
                elif ("turn on" in line[:line.index(temp[0])]):
                    grid[i][j]+=1
                elif ("toggle" in line[:line.index(temp[0])]):
                    grid[i][j]+=2

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            res+=grid[i][j]

    sys.stdout.write("Total brightness: {}".format(res))

if __name__=="__main__":
    main()