
data = open("test.txt")
data = open("data.txt")


lines = []
for line in data:
    pos, vector = line.strip("\n").split("@")
    x,y,z = map(int, pos.split(","))
    dx,dy,dz = map(int, vector.split(","))
    lines.append((x,y,z,dx,dy,dz))

from sympy import Symbol, solve_poly_system

x = Symbol("x")
y = Symbol("y")
z = Symbol("z")
dx = Symbol("dx")
dy = Symbol("dy")
dz = Symbol("dz")
t1 = Symbol("t1")
t2 = Symbol("t2")
t3 = Symbol("t3")

f1 = x+dx*t1 - lines[0][0] - lines[0][3]*t1
f2 = y+dy*t1 - lines[0][1] - lines[0][4]*t1
f3 = z+dz*t1 - lines[0][2] - lines[0][5]*t1
f4 = x+dx*t2 - lines[1][0] - lines[1][3]*t2
f5 = y+dy*t2 - lines[1][1] - lines[1][4]*t2
f6 = z+dz*t2 - lines[1][2] - lines[1][5]*t2
f7 = x+dx*t3 - lines[2][0] - lines[2][3]*t3
f8 = y+dy*t3 - lines[2][1] - lines[2][4]*t3
f9 = z+dz*t3 - lines[2][2] - lines[2][5]*t3
res = solve_poly_system([f1, f2, f3, f4, f5, f6, f7, f8, f9], [x,y,z,dx,dy,dz,t1,t2,t3])
print(res)
print(res[0][0] + res[0][1] + res[0][2])