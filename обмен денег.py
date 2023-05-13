f=open("C:/Users/Алина/Desktop/13.txt")
ds1=list(map(int,f.readline().strip().split()))
ch1=list(map(int,f.readline().strip().split()))
ds2=list(map(int,f.readline().strip().split()))
ch2=list(map(int,f.readline().strip().split()))
dengi1=list(map(int,f.readline().strip().split()))
kop = 0
a=0
dengi2=[0 for i in range (ds2[0]) ]
for j in range(len(dengi1)):
    sch=dengi1[j]
    for i in range(1,ch1[0]+1):
        if sch>ch1[i]:
            dengi1[j]-=1
for i in range (1,ds1[0]):
    a= (a+dengi1[i-1])*ds1[i]
kop = dengi1[-1]+a
ds2.reverse()
for i in range(len(ds2)-1):
    dengi2[-i-1]=kop % ds2[i]
    kop=kop//ds2[i]
dengi2[0]=kop
ch2=ch2[1:-1]
ch2.sort()
for j in range(len(dengi2)):
    for i in range(len(ch2)):
        if dengi2[j]>ch2[i]:
            dengi2[j]+=1
print(dengi2)












