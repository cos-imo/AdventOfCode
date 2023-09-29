import sys

def check(lst):
    for i in range(0,len(lst)-1):
        if lst[i] in (lst[:i]+lst[(i+1):]):
            return False
    return True

def main():
    file=open('input','r')
    lst=file.readlines()

    for i in range(4,len(lst[0])-1):
        if check(lst[0][i-4:i]):
            print(i)
            break

if __name__=="__main__":
    main()
