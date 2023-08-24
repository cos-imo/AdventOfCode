import sys, copy, operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
    '>' : operator.gt,
    '<' : operator.lt,
    '==' : operator.eq,
    '<=' : operator.le,
    '>=' : operator.ge,
    '!=' : operator.ne
}

def main():

    global ops

    file=open('input','r')
    data=[element.replace('\n','').split(' ') for element in file.readlines()]

    registers={}

    for instruction in data:
        if not (instruction[0] in registers):
            registers[instruction[0]]=0
        if not (instruction[4] in registers):
            registers[instruction[4]]=0
        if ops[instruction[5]](registers[instruction[4]], int(instruction[-1])):
            if instruction[1]=="inc":
                registers[instruction[0]]+=int(instruction[2])
            elif instruction[1]=="dec":
                registers[instruction[0]]-=int(instruction[2])
            else:
                sys.stdout.write("Compilation ERROR: instruction not recognized\nline {} - {}\n  ^^^\nExiting".format(data.index(instruction), instruction.join(' ')))    

    sys.stdout.write("End of computations.\nThe register with the higher value is register {}.\nValue: {}\n".format(max(registers, key= lambda x: registers[x]),registers[max(registers, key= lambda x: registers[x])]))

if __name__=="__main__":
    main()