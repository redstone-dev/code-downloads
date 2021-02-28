maxdepth = 100
rndlist = []

def rand(k1,k2,n):
    for i in range(0, 10):
        return ((((k1+i) + (n ^ k2)) - k2 + (n ^ k1)) - (n + (k2 ^ k1)))

for x in range(1234):
    rndlist.append(rand(x,x+3412,x-3412))

for y in range(len(rndlist)):
    print(-(rndlist[y] ^ -rndlist[y]))