def BellmanFord(mapa, s, N):
	# inicializamos el grafo. Ponemos distancias a INFINITO menos el nodo origen que 
	# tiene distancia 0
	distancia = [float('inf')]*N
	predecesor = [None]*N

	distancia[s]=0;
	# relajamos cada arista del grafo tantas veces como número de nodos -1 haya en el grafo
	for i in range(1,N):
		for u, v, dist in mapa:
			if distancia[v]>distancia[u] + dist:
				distancia[v] = distancia[u] + dist
				predecesor[v] = u

	# comprobamos si hay ciclos negativo
	for u, v, dist in mapa:
		if distancia[v] > distancia[u] + dist:
			return True

	return False

c = int(input())

for i in range(c):
	n, m = map(int,input().split())
	mapa = []

	for j in range(m):		
		x,y,t = map(int,input().split())
		mapa.append([x,y,t])

	
	if m > 0:
		BF = BellmanFord(mapa,0,n)

		if BF:
			print("possible")
		else:
			print("not possible")
	else:
		print("not possible")
	
