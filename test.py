
from collections import Counter
z = [1,2,2,3,3,5]
flag=0
size = len(z)//2
print(size)
c = Counter(z)
print(c)
d=c.values()
e= list(d)
# print(e)
for num in e:
    # print(num)
    if num > size:
        flag=1
        break;
if flag:
    print("True")
else:
    print("False")
    
        




  