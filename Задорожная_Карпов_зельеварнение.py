f=open("C:/Users/User/Desktop/13.txt")
a=f.readlines()
list={}
zaklinanie=""
for i in range(len(a)):
    komp=a[i].strip().split()
    for j in range(len(komp)):
        if komp[j] in list:
            komp[j]=list[komp[j]]
    s=""
    for j in range(1, len(komp)):
        s+=komp[j]
    if komp[0]=="DUST":
        list[str(i+1)]="DT"+s+"TD"
    if komp[0]=="FIRE":
        list[str(i+1)]="FR"+s+"RF"
    if komp[0]=="WATER":
        list[str(i+1)]="WT"+s+"TW"
    if komp[0]=="MIX":
        list[str(i+1)]="MX"+s+"XM"
print(list[str(len(a))])