# get coordinates of every position the line will ever be in and return it as a list of xy pairs
# compare lists
# find which is closest to (0,0)
import math

def readfile():
    f = open('AOCDAY3.txt', 'r')
    flist = f.read().split('\n')
    dirlists = []
    for i in flist:
        i = i.split(',')
        dirlists.append(i)
    dirlists.pop()
    return dirlists


def get_all_coords(directions):
    all_coords = []
    pos = (0,0)
    for cmd in directions:
        if cmd[0] == 'U':
            for i in range(int(cmd[1:])):
                tup = (pos[0],pos[1] + 1)
                all_coords.append(tup)
                pos = tup
        elif cmd[0] == 'D':
            for i in range(int(cmd[1:])):
                tup = (pos[0],pos[1] - 1)
                all_coords.append(tup)
                pos = tup
        elif cmd[0] == 'R':
            for i in range(int(cmd[1:])):
                tup = (pos[0] + 1,pos[1])
                all_coords.append(tup)
                pos = tup
        elif cmd[0] == 'L':
            for i in range(int(cmd[1:])):
                tup = (pos[0] - 1,pos[1])
                all_coords.append(tup)
                pos = tup
        all_coords.append(tup)
        pos = tup
    return all_coords


def find_closest(l1, l2):
    crosses = []
    if (set(l1) & set(l2)):
        crosses = (set(l1) & set(l2))
        # print(crosses)
        manhattan = []
        for i in crosses:
            manhattan.append(math.fabs(i[0])+math.fabs(i[1]))
        # print(manhattan)
        return int(min(manhattan))


def main():
    direction_set = readfile()
    line_1 = get_all_coords(direction_set[0])
    line_2 = get_all_coords(direction_set[1])
    # line_1 = get_all_coords(['R8','U5','L5','D13'])
    # line_2 = get_all_coords(['U7','R6','D14','L4'])
    closest = find_closest(line_1, line_2)
    print(closest)


if __name__ == '__main__':
    main()
