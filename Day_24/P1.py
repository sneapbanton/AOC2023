import numpy as np

data = open("test.txt")
test_area = (7,27)
if True:
    data = open("data.txt")
    test_area = (200000000000000, 400000000000000)


lines = []
for line in data:
    pos, vector = line.strip("\n").split("@")
    x,y,z = map(int, pos.split(","))
    dx,dy,dz = map(int, vector.split(","))
    lines.append((x,y,z,dx,dy,dz))


"""
---------------
Borrowed forum code for intersecting lines
"""
def perp( a ) :
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

def seg_intersect(a1,a2, b1,b2) :
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = perp(da)
    denom = np.dot( dap, db)
    num = np.dot( dap, dp )
    return (num / denom.astype(float))*db + b1

"""
---------------
"""

counter = 0
for i in range(len(lines)-1):
    ax,ay,az,adx,ady,adz = lines[i]
    p1 = np.array([ax + adx*int((test_area[0] - ax)/adx), ay + ady*int((test_area[0] - ay)/ady)])
    p2 = np.array([ax + adx*int((test_area[1] - ax)/adx), ay + ady*int((test_area[1] - ay)/ady)])
    if ax in range(test_area[0],test_area[1]+1):
        if adx < 0:
            p2[0] = ax
        else:
            p1[0] = ax
    if ay in range(test_area[0],test_area[1]+1):
        if ady < 0:
            p2[1] = ay
        else:
            p1[1] = ay
    for j in range(i+1, len(lines)):
        bx,by,bz,bdx,bdy,bdz = lines[j]
        p3 = np.array([bx + bdx*int((test_area[0] - bx)/bdx), by + bdy*int((test_area[0] - by)/bdy)])
        p4 = np.array([bx + bdx*int((test_area[1] - bx)/bdx), by + bdy*int((test_area[1] - by)/bdy)])
        if bx in range(test_area[0],test_area[1]+1):
            if bdx < 0:
                p4[0] = bx
            else:
                p3[0] = bx
        if by in range(test_area[0],test_area[1]+1):
            if bdy < 0:
                p4[1] = by
            else:
                p3[1] = by
        
        pa = np.array([ax,ay])
        pb = np.array([ax+adx, ay+ady])
        pc = np.array([bx,by])
        pd = np.array([bx+bdx, by+bdy])
        res = seg_intersect(pa,pb,pc,pd)
        if p1[0]<=res[0]<=p2[0] and p3[0]<=res[0]<=p4[0] and p1[1]<=res[1]<=p2[1] and p3[1]<=res[1]<=p4[1]:
            counter += 1

print(counter)