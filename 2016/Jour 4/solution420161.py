import sys, copy, string

def main():

    file=open('input','r')
    raw_data=file.readlines()

    alphabet=string.ascii_lowercase
    
    first_split=[element.split("[") for element in raw_data]
    first_split=[[element0, element1.replace(']','').replace("\n",'')] for [element0, element1] in first_split]
    codes=[int(element[-3:]) for [element, garbage] in first_split]

    characters=[element.split("-")[:-1] for [element, garbage] in first_split]

    total=0

    for element in characters:
        counter=[(''.join(element)).count(character) for character in alphabet]
        reconstitued=''.join(element)
        res=[]
        for letter in reconstitued:
            counter[alphabet.index(letter)]+=1
        for i in range(5):
            res.append(alphabet[counter.index(max(counter))])
            counter[counter.index(max(counter))]=0
        total+=((''.join(res))==first_split[characters.index(element)][-1])*codes[characters.index(element)]

    sys.stdout.write("\n\t=> Sum of the sector IDs of the real rooms: " + str(total) + "\n\n")

if __name__=="__main__":
    main()