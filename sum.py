sum_list=[1,2,3,5,-4]
sum=0
for i in range(len(sum_list)):
    sum+=sum_list[i]
print(sum)
prod=1
for i in range(len(sum_list)):
    prod*=sum_list[i]
print(prod)
largest=sum_list[0]
for i in range(len(sum_list)):
    if largest<sum_list[i]:
        largest=sum_list[i]
print(largest)