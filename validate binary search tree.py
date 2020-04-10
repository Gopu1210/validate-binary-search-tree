i = int(input("enter the no of nodes: "))
In=[]
flag=False
for i in range(i):
    In.append(int(input()))
print(In)
if(len(In)==3):
        if(In[1]<In[0] and In[2]>In[0]):
            flag=True
for i in range(0,len(In)-3):
    if(In[i+1]<In[i] and In[i+2]>In[i]):
        flag=True
    break
print(flag)
