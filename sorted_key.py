def last(n): return n[-1]

def sort_list_last(sample): 
    return sorted(sample,key=last) #A custom key function can be supplied to customize the sort order, and the reverse flag can be set to request the result in descending order.

print(sort_list_last([(2,5),(1,2),(4,4),(2,3),(2,1)]))