import string
import random
arr=string.ascii_lowercase

arra=[]

ln=6
for i in range(0,(26**ln)):
    strrnd=""
    while True:
        for j in range(0,ln):
            rnd1=random.randint(0,25)
            strrnd=strrnd+arr[rnd1]
        if strrnd not in arra:
            arra.append(strrnd)
            break
        
print("Succesful")