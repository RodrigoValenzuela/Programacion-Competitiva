def BFS(mapa,n,s):
	estado = [False]*(n+1)
	distancia = [float('inf')]*(n+1)
	padre = [None]*(n+1)
	flujo = float('inf')

	estado[s] = True
	distancia[s] = 0

	Cola = []
	Cola.append(s)

	while Cola:
		u = Cola.pop(0)

		for vecino,costo in mapa[u]:
			if not estado[vecino] and costo > 0:
				estado[vecino] = True
				distancia[vecino] = distancia[u]+1
				padre[vecino] = u
				Cola.append(vecino)
				if costo < flujo:
					flujo = costo

	return padre,flujo

def HacerRuta(lista,s,t):
	ruta = [t]
	actual = lista[t]
	#print(actual)

	while actual != s:
		ruta.insert(0,actual)
		actual = lista[actual]
		#print(actual)

	ruta.insert(0,s)
	return ruta

def Rutas(mapa,n,s,t,red):
	siguiente = 1
	pesos = 0

	print("Network "+str(red))
	#archivo.write("Network "+str(red)+"\n")
	while True:

		padre, flujo = BFS(mapa,n,s)
		#print(padre, flujo)

		if padre[t] != None:
			ruta = HacerRuta(padre,s,t)
			#print(ruta,flujo)
		else:
			#No hay camino disponible
			print("The bandwidth is "+ str(pesos) + ".\n")
			#archivo.write("The bandwidth is "+ str(pesos) + ".\n\n")
			break

		pesos += flujo
		#archivo.write("Restando " + str(flujo) + ".\n")
		#print(ruta)

		actual = ruta.pop()

		
		for i in range(len(ruta)):
			siguiente = ruta.pop()

			for j in range(len(mapa[siguiente])):
				camino, costo = mapa[siguiente][j]
				if camino == actual and costo >= flujo:
					mapa[siguiente][j][1] -= flujo
					break

			for j in range(len(mapa[actual])):
				camino, costo = mapa[actual][j]
				if camino == siguiente and costo >= flujo:
					mapa[actual][j][1] -= flujo
					break

			actual = siguiente
                
		#print(mapa)

#En caso de imprimir fuera de terminal
#archivo = open("output.txt", "w")

n = int(input())
red = 1

while n != 0:

	mapa = [[]]*(n+1)
	s, t, conexiones = map(int,input().split())

	for i in range(conexiones):
		a, b, c = map(int,input().split())
	
		if mapa[a] == []:
			mapa[a] = [[b,c]]
		else:
			mapa[a].append([b,c])
		if mapa[b] == []:
			mapa[b] = [[a,c]]
		else:
			mapa[b].append([a,c])

	Rutas(mapa,n,s,t,red)
	red += 1
		
	n = int(input())

#archivo.close()
