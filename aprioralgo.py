lst=[['a','b','c'],['b','c','d'],['g','c','d'],['x','y','z','c','d']]
indilst=[]
lstlen=len(lst)
for i in lst: 
  for j in i:
    if j not in indilst:  
      indilst.append(j)
print("main list")
print(lst)      #main list
print("individual list")
print(indilst)  #all in 1 list

f=[]
ct=0
for a in indilst: 
  for b in lst:
    for c in b:
      if(c==a):  # a==a
        ct=ct+1  # count
  f.append(ct)   # f=1
  ct=0
print("frequency")
print(f)  # [1,4....]


temp=[]
lsttemp=[]
indilstlen=len(indilst)  #lenght of indilist = 8
i=0
while(i<indilstlen):
  if(f[i]>=2):   #threshold 1>=2
    lsttemp.append(indilst[i]) #b  
    temp.append(f[i]) #2
  i=i+1
indilst=lsttemp  # indilst=b
f=temp	# f=2
print("threshold individual list")
print(indilst) #b
print("threshold frequency")
print(f) #2


lenf =len(f)-1  # 3-1=2  
i=0 
for i in range(lenf):  #sorting of 1,2,3.. i,e 2,4,3 
  while(f[i]<f[i+1]):
    temp=f[i+1]
    f[i+1]=f[i]
    f[i]=temp
     
    t=indilst[i+1]  #sorting of a,b,c.. i.e c,d,b
    indilst[i+1]=indilst[i]
    indilst[i]=t
print("sorted individual list")
print(indilst)
print("sorted frequency")
print(f)



indilstlen=len(indilst) #3
newlist=[]
for i in range(0,indilstlen): #b  ['c', 'd', 'b']
  for t in range(i+1,indilstlen): #c 
    templst=[] #[c,d]
    templst.append(indilst[i]) #c push
    templst.append(indilst[t]) #d push
    newlist.append(templst)
print("cluster")
print(newlist) 


f2=[]
ct=0
newlstlen=len(newlist) #3
i=0
while(i<newlstlen):
  temp=newlist[i] 
  for j in lst: # main list
    if(temp[0] in j): #c
      if(temp[1] in j): #d
        ct=ct+1 
  f2.append(ct) 
  i=i+1
  ct=0
print("cluster frequency")
print(f2)  #count the newlist


f2len=len(f2) #3
i=0
while(i<f2len): 
  if(f2[i]<2): #threshold
    f2.pop(i) #less than pop i.e 1
    newlist.pop(i) #less than pop i.e d,b
  i=i+1
print("threshold cluster")
print(newlist)
print("threshold frequency")
print(f2)   
  






    