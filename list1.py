list_a=['RNM','AHR','SES','ES','MLDM']
x=list_a.pop(2)
print(x)
print(list_a)

cubes=[x**3 for x in range(10)]
print(cubes)

a=[(x,y) for x in [1,3,4] for y in [2,3,4] if x!=y]
print(a)

from math import pi
b=[(round(pi,i)) for i in range(1,4)]
print(b)

list_b=['sanjay','yadav','tamilnadu']
del list_b