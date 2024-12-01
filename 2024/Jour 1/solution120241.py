import re

def main():
    with open('input','r') as file:
        data = [line.replace('\n', '') for line in file.readlines()]

    splitted = [re.findall(r'(\d+)\s+(\d+)', line)[0] for line in data]
    list1, list2 = [element[0] for element in splitted], [element[1] for element in splitted]

    res = 0

    while(list1):
        res += abs(int(list1.pop(list1.index(min(list1)))) - int(list2.pop(list2.index(min(list2)))))


    print(f"The total distance between the lists is: {res}")


if __name__=="__main__":
    main()
