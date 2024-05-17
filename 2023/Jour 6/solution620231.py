def main():
    with open("input", "r") as file:
        data = [(element.replace("\n", "")).split(" ") for element in file.readlines()]

    times, distances= [[int(element) for element in sublist if element.isdigit()] for sublist in data]

    possibilities = [[i*(time-i) for i in range(time)] for time in times]

    result = 1

    for race in possibilities:
        result *= len([element for element in race if element>distances[possibilities.index(race)]])

    print(f"\n\n\tThe product of the number of ways you can win each race is: {result}\n\n")

if __name__ == "__main__":
    main()
