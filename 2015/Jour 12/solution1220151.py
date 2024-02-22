import sys, copy, re

def main():
    with open("input", "r") as file:
        data = file.readlines()

    numbers=0

    for line in data:
        numbers+=sum([int(element) for element in (re.findall(r'[-]?\d+', line))])

    sys.stdout.write(f"The numbers in this document add up to {numbers}\n")

if __name__=="__main__":
    main()
