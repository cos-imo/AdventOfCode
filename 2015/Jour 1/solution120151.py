import sys

def main():

    file=open('input','r')                          #Ouverture du fichier d'input
    lst=file.readlines()

    c=0

    for line in lst:
        for element in line:
            if element=='(':
                c+=1                                       #Lorsquel'on rencontre une ligne vide, on ajoute un nouvel elfe
            elif element==')':
                c-=1
            
    sys.stdout.write("Santa has to go to floor " + str(c))

if __name__=="__main__":
    main()

