import numpy as np

def B3(dataset, n):
    space = []

    data = dataset

    for line in data:
        line = line.strip("\n")
        line = list(line)
        space.append(line)

    space = np.array(space)
    rows, cols = space.shape
    

    r = 0
    while r < rows:
        if len(set(space[r,:])) == 1:
            space = np.delete(space, r, axis=0)
            space = np.insert(space, r, "-", axis=0)
        r += 1

    c = 0
    while c < cols:
        if set(space[:,c]) == set([".", "-"]):
            space = np.delete(space, c, axis=1)
            space = np.insert(space, c, "|", axis=1)
        c += 1


    nodes = []
    for r in range(rows):
        for c in range(cols):
            if space[r,c] == "#":
                nodes.append((r,c))
            elif space[r,c] == "|" and 0<r<rows-1 and 0<c<cols-1 and space[r-1,c]==space[r+1,c]=="|" and space[r,c-1]==space[r,c+1]=="-":
                space[r,c] = "+"

    def traverser(start, goal, n):
        sr, sc = start
        gr, gc = goal
        r = sr
        c = sc
        steps = 0
        step_r = int((gr-sr) / max(1, abs(gr-sr)))
        step_c = int((gc-sc) / max(1, abs(gc-sc)))
        
        while r != gr:
            if space[r,c] == "-":
                steps += n
            else:
                steps += 1
            r += step_r
        while c != gc:
            if space[r,c] == "|":
                steps += n
            else:
                steps += 1
            c += step_c
        return steps
        

    result = 0
    for i in range(len(nodes)):
        for j in range(i, len(nodes)):
            if (i != j):
                result += traverser(nodes[i], nodes[j], n)

    return result


if __name__=="__main__":
    test_data = open("test.txt")
    data = open("data.txt")
    assert(B3(test_data, 10) == 1030)
    test_data = open("test.txt")
    assert(B3(test_data, 100) == 8410)
    print(B3(data, 1000000))