
def find(n):
	global parents
	if parents[n] == n:
		result = n
	else:
		result = find(parents[n])
		parents[n] = result
	return result

def kruskal():
	global N, parents
	arcos = []
	for n in range(len(N)):
		for m in range(n+1, len(N)):
			arcos.append((distance(N[n], N[m]), n, m))
	arcos = sorted(arcos)
	n_arcos = []
	for w, u, v in arcos:
		if find(u) != find(v):
			parents[find(v)] = find(u)
			n_arcos.append(w)
	return n_arcos

N = []
parents = [n for n in range(len(N))]
