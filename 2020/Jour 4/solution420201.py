import sys, copy, operator

def main():

    file=open('input','r')
    data=[line.replace('\n','') for line in file.readlines()]

    count=0
    current_elements=[0 for i in range(8)]
    current_elements[-1]=1
    fields=["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]

    for element in data:
        if element=='':
            count+=all(current_elements)
            current_elements=[0 for i in range(8)]
            current_elements[-1]=1
        else:
            temp=element.split(' ')
            for element in temp:
                temp[temp.index(element)]=(element.split(":"))[0]
            for elementi in temp:
                current_elements[fields.index(elementi)]=1
    count+=all(current_elements)
    sys.stdout.write("Data processed. {} valid passports \n".format(count))
    

if __name__=="__main__":
    main()