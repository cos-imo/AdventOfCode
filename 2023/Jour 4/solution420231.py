import re, sys

def main():
    with open('input','r') as file:
        data=[element[9:].replace('\n','').split(("|")) for element in file.readlines()]

    res=0

    for entry in data:
        player_numbers, winning_numbers = [int(i) for i in entry[0].split(' ') if i!=''], [int(i) for i in entry[1].split(' ') if i!='']
        res+=(int(2**(sum([1 for number in player_numbers if number in winning_numbers])-1)*(sum([1 for number in player_numbers if number in winning_numbers])!=0)))

    sys.stdout.write("The given  dexk of cards is worth " + str(res) + " points")

if __name__=="__main__":
    main()
