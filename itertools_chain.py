import itertools

or_list=[[1,2,3],[4,5,6,7],[9],[9,10]]
new=list(itertools.chain(*or_list))
print(new)