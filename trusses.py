from sys import argv

def size_of_intersection(s1, s2, g):
	counter = 0
	for i in g[s1]:
		for j in g[s2]:
			if g[i] == g[j]:
				counter = counter + 1
	return counter

def remove(s1, s2, g):
	for v in g[s1]:
	 	if s2 ==v:
	 		g[s1].remove(s2)
	for j in g[s2]:
		if s1==j:
			g[s2].remove(s1)
	return 

def trussesMeth(g, k):
	for i in range(0,10):
		for key in g:
			for value in g[key]:
				if size_of_intersection(key, value, g) < k-2:
					remove(key, value, g)
	return			
	
def print_result(g,k):
	result = {}
	grafosT = {}
	counter = 0		
	for key in g:
		lista = (g[key] + [key])
		if len(lista) > k-2:
			lista.sort()
			grafosT[counter] = lista
			counter = counter + 1

	for key,value in sorted(grafosT.items(), key=lambda e: e[1][2]):
		if value not in result.values():
			result[key] = grafosT[key]
			keimeno = ', '.join(str(x) for x in result[key])
			print('(' + keimeno + ')')	
	return

arg1, arg2, arg3 = argv

f = open(arg2)
k = int(arg3)

komvoi = []
grafos = {}
komv = 0

for line in f:
	x, y = map(int, line.strip().split(' '))
	if x not in komvoi:
		komvoi.append(x)
		grafos[x] = [y]
	else:
		grafos[x].append(y)
	if y not in komvoi:
		komvoi.append(y)
		grafos[y] = [x]
	else:
		grafos[y].append(x)
trussesMeth(grafos, k)
print_result(grafos, k)

f.close() 