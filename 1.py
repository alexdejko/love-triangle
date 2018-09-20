a=[6, 14, 12, 21, 3, 20, 7, 15, 16, 16, 14, 4, 11, 13, 18, 2, 1, 8, 3, 1, 12]
# x=0
# for i in range(1,len(a)+1):
# 	if (a[i-1]==a[a[a[a[i-1]-1]-1]-1] and 
# 		a[i-1]!= a[a[i-1]-1] and
# 		a[i-1]!= a[a[a[i-1]-1]-1]):
# 		x+=1
# 	print(a[i-1],a[a[i-1]-1],a[a[a[i-1]-1]-1],a[a[a[a[i-1]-1]-1]-1],a[a[a[a[a[i-1]-1]-1]-1]-1],a[a[a[a[a[a[i-1]-1]-1]-1]-1]-1])
# 	a[i-1]=-1
# print(int(x))


nodes = {n+1:i for n,i in enumerate(a)}
print(nodes)
c=0
for i in list(nodes):
	if i in nodes:
		j = nodes[i]
		if j in nodes:
			k = nodes[j]
			if i == nodes.get(k) and i != j and j != k:
				c+=1
				del nodes[i]
				del nodes[j]
				del nodes[k]
print(c)