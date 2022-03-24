counts = dict()
names = ['c','cw','cw']
for name in names:
    if(name not in counts):
        counts[name]=1
    else:
        counts[name] = counts[name]+1

print(counts)
