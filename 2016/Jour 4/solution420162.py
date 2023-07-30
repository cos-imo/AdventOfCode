import sys, copy, string

def main():

    file=open('input','r')
    raw_data=file.readlines()

    alphabet=string.ascii_lowercase
    
    first_split=[element.split("[") for element in raw_data]
    first_split=[[element0, element1.replace(']','').replace("\n",'')] for [element0, element1] in first_split]
    codes=[int(element[-3:]) for [element, garbage] in first_split]

    characters=[element.split("-")[:-1] for [element, garbage] in first_split]

    tab=[[[alphabet[(alphabet.index(letter)+(codes[characters.index(element_list)]))%26] for letter in element] for element in element_list] for element_list in characters]

    """for lst in tab:
        sys.stdout.write(str(tab.index(lst)) + " - ")
        for element in lst:
            for char in element:
                sys.stdout.write(char)                              #output: look out for "northpole object storage". Mine is line 947!
            sys.stdout.write(" ")
        sys.stdout.write("\n")"""

    print("\n\t=> Room ID: " + str(first_split[947][0][-3:]) + "\n")

    #sys.stdout.write(first_split[])

if __name__=="__main__":
    main()