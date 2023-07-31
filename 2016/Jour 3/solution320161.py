import sys, copy

def main():

    file=open('input','r')
    raw_data=file.readlines()
    formatted_data=[]

    total=0
    phrase=["La ligne ne correspond pas à un triangle", "La ligne correspond à un triangle"]

    history=[]

    for raw_line in raw_data:
        formatted_data.append(raw_line.split(" "))
    
    for original_splitted_line in formatted_data:
        splitted_line = copy.deepcopy(original_splitted_line)
        splitted_line=[int(element) for element in splitted_line if element]
        total+=(((splitted_line[0]<(splitted_line[1]+splitted_line[2]))) and ((splitted_line[1])<(splitted_line[0]+splitted_line[2])) and (splitted_line[2]<(splitted_line[1]+splitted_line[0])))
        
        """
        print("\n\n" + phrase[(((splitted_line[0]<(splitted_line[1]+splitted_line[2]))) and ((splitted_line[1])<(splitted_line[0]+splitted_line[2])) and (splitted_line[2]<(splitted_line[1]+splitted_line[0])))])
        print("Verification:")
        print("Données: " + str(splitted_line[0]) + " " + str(splitted_line[1]) + " " + str(splitted_line[2]))
        sys.stdout.write(str(splitted_line[0]) + "<" + str(splitted_line[1]) + "+" + str(splitted_line[2]) + "=" + str(splitted_line[1]+splitted_line[2]) + " is ")
        print((((splitted_line[0]<(splitted_line[1]+splitted_line[2])))))
        sys.stdout.write(str(splitted_line[1]) + "<" + str(splitted_line[0]) + "+" + str(splitted_line[2]) + "=" + str(splitted_line[0]+splitted_line[2]) + " is ")
        print(((splitted_line[1])<(splitted_line[0]+splitted_line[2])))
        sys.stdout.write(str(splitted_line[2]) + "<" + str(splitted_line[1]) + "+" + str(splitted_line[0]) + "=" + str(splitted_line[1]+splitted_line[0]) + " is ")
        print((splitted_line[2]<(splitted_line[1]+splitted_line[0])))
    print(total)
    print(history)
    """
        
    sys.stdout.write("\n\t=> Number of valid triangles: {} \n\n".format(total))


if __name__=="__main__":
    main()