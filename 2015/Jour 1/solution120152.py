import sys

def main():

    file=open('input','r')                          #Ouverture du fichier d'input
    lst=file.readlines()

    c=0

    for line in lst:
        for i in range(len(line)):
            if c==-1:
                sys.stdout.write(str(i))
                return
            elif line[i]=='(':
                c+=1                                       #Lorsquel'on rencontre une ligne vide, on ajoute un nouvel elfe
            elif line[i]==')':
                c-=1
            
    sys.stdout.write("Santa goes to basement on instruction " + str(c))

if __name__=="__main__":
    main()

