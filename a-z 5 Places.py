import string
import time
a=string.ascii_lowercase
flobj=open("D:/ioph1.txt","w")
arr=[]
t1=time.time()
for i in range(0,26):
    for j in range(0,26):
        for k in range(0,26):
            for l in range(0,26):
                for m in range(0,26):
                    strs=a[i]+a[j]+a[k]+a[l]+a[m]
                    strs=strs+"\n"
                    flobj.write(strs)
t2=time.time()
flobj.close()
print(t2-t1)