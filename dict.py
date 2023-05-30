knights={'Bahubali':'the great','Kattapa':'the dhrogi'}
for k,v in knights.items():
    print(k,v)

for i,v in enumerate(['tic','tac','toe']):
    print(i,v)

questions=['name','team','marital stat']
answers=['bahubali','team good','married']
for q,a in zip(questions,answers):
    print('What is your {0}? It is {1}.'.format(q,a))