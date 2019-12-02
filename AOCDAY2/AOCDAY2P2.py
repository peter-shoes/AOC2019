# import functions from part 1
import AOCDAY2P1


def opcode_instruction(intcode):
    # desired output
    req_output = 19690720
    # which noun and verb will produce the desired output
    # testing integers 0-99, specified by the puzzle
    for noun in range(100):
        for verb in range(100):
            intcode[1] = noun
            intcode[2] = verb
            intcode = AOCDAY2P1.opcode_reader(intcode)
            # test condition
            if intcode[0] == req_output:
                return(noun, verb)
            else:
                # reset intcode
                intcode = AOCDAY2P1.readfile()


def main():
    # get intcode
    intcode = AOCDAY2P1.readfile()
    solution = opcode_instruction(intcode)
    # the puzzle requires the solution in the following form
    puzzle_solution = 100*solution[0]+solution[1]
    print(puzzle_solution)
    return puzzle_solution


if __name__ == '__main__':
    main()
