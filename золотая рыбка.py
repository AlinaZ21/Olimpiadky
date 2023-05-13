f=open("C:/Users/Алина/Desktop/13.txt")
n=int(f.readline())
a1=[]
for i in range(n):
   a1.append(f.readline().strip())
n=int(f.readline())
nach={}
nac=""
for i in range(n):
   q,w=f.readline().strip().split()
   nach[q]=[int(w), 0]
   nac+=q
kon={}
ko=""
n=int(f.readline())
for i in range(n):
   q,w=f.readline().strip().split()
   kon[q]=[int(w), 0]
   ko+=q
a=[]
for i in a1:
   if i[0] in nac and i[-1] in ko:
      a.append(i)
for i in a:
   nach[i[0]][1]+=1
   kon[i[-1]][1]+=1
s=0
for i in nach:
   s+=min(nach[i])
p=0
for i in kon:
   p+=min(kon[i])
print(min(s,p))