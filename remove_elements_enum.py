sample=['Red','Blue','Green','Yellow','Orange']
sample=[s for (i,s) in enumerate(sample) if i not in (0,1,3)]
print(sample)

num_list=[1,2,3,4,5,6,7,8,9,10]
num_list=[num for num in num_list if num%2 is not 0 ]
print(num_list)