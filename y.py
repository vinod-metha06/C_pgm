R=int(input());
m=[];
d={}
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(R):      # A for loop for column entries
         a.append(int(input()))
    m.append(a)
    
for i in range(R):
    for j in range(R):
        f=m[i][j]
        v={f:0}
        d.add(v)
       # d[f] = 0
        #print(m[i][j], end = "");
    #print("\n")

for x ,y in d.items():
    print(x,y)
