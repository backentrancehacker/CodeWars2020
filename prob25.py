#fun times
import math
querycount = input()
num, query = querycount.split()

xlist = []
ylist = []
namelist = []

num = int(num)
query = int(query)

for i in range(0, num):
    #do shit
    string = input()
    number, name = string.split()
    n = 2
    x, y = [number[k:k+n] for k in range(0, len(number), n)]
    x = int(x)
    y = int(y)
    xlist.append(x)
    ylist.append(y)
    namelist.append(name)

for i in range(0, query):
    jump = input()
    leave, arrive = jump.split()
    
    out = []
    to = []
    
    for d in range(0, len(namelist)):
        var = namelist[d]
        if var == leave:
            out.append(xlist[d])
            out.append(ylist[d])
            
        elif var == arrive:
            to.append(xlist[d])
            to.append(ylist[d])
            
    x1 = int(out[0])
    x2 = int(to[0])
    y1 = int(out[1])
    y2 = int(to[1])
    du = x2 - x1
    dv = (y2 + x2 // 2) - (y1 + x1 // 2)
    distance = max(abs(du), abs(dv)) if ((du >= 0 and dv >= 0) or (du < 0 and dv < 0)) else abs(du) + abs(dv)
    print(jump, distance)