# read the file into the program
def readfile():
    f = open('AOCDAY2.txt', 'r')
    flist = f.read().split(',')
    flist[-1] = flist[-1][:-1]
    intlist = []
    for i in flist:
        intlist.append(int(i))
    return intlist


def opcode_reader(intcode,pos=0):
    # get current opcode
    opcode = intcode[pos]
    # set position values for the opcode to operate on
    val1_pos = intcode[pos+1]
    val2_pos = intcode[pos+2]
    val3_pos = intcode[pos+3]
    # opcode case 1
    if opcode == 1:
        opcode_process_result = intcode[val1_pos]+intcode[val2_pos]
        intcode[val3_pos] = opcode_process_result
        pos +=4
        return opcode_reader(intcode, pos)
    # opcode case 2
    elif opcode == 2:
        opcode_process_result = intcode[val1_pos]*intcode[val2_pos]
        intcode[val3_pos] = opcode_process_result
        pos +=4
        return opcode_reader(intcode, pos)
    # opcode case 99
    elif opcode == 99:
        return intcode



def main():
    # get intcode
    intcode = readfile()
    # problem specification for "1202 program alarm"
    intcode[1] = 12
    intcode[2] = 2
    # translate intcode
    updated_intcode = opcode_reader(intcode,0)
    print(updated_intcode[0])


if __name__ == '__main__':
    main()
