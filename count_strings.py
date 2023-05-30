sample=['abc','xyx','aba','1221']
count=0
for samp in sample:
    if len(samp)>1 and samp[0]==samp[-1]:
        count+=1
print(count)