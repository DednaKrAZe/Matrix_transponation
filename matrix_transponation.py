size=input()
size=size.split()
strings=[]
for i in range (0,int(size[0])):
    nums=input()
    nums=nums.split()
    strings.append((nums))

for j in range (0,int(size[1])):
    line=''
    for k in range(int(size[0])-1,-1,-1):
        line+=strings[k][j]
        if k!=0:
            line+=' '
    print(line)