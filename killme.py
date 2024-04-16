def minmax(lista):
    if isinstance(lista, list) and len(lista)>2:
        return minmax_aux(lista, 0, 0, 0, [])
    else:
        return "Error"
def minmax_aux(lista, n,  minimo, maximo, new):
    if lista == []:
        return new
    elif lista[n] > maximo:
        maximo = lista[n]
        new
        return lista, n+1, minimo, maximo, new

print("help")
