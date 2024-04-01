lista = [1,3,9,4,2,5,7,0,6,8]
lista[3] = 1#muda o valor do elemento 3 da lista
lista.append(10)#adiciona um elemento a lista
lista.sort()#Arruma a ordem da lista
lista.sort(reverse=True)#colocar a ordem reversa
lista.insert(1,5)#insiro valor na posição delimitada
lista.pop()#elimina um elemento
lista.remove(2)#elimina a primeira aparição do elemento se não tiver use o if e else
#Exemplo
n = []
n.append(2)
n.append(3)
n.append(4)
for c,v in enumerate(n):
    print(f"Na posição {c} tem o numero {v}")
#Pode-se usar tambem
for cont in range(0,6):
    n.append(int(input("digite um numero")))
#outro caso
a = [1,2,3,4]
#b = a#isso faz uma ligação
b = a[:]#isso copia os itens de 'a' para 'b'
b[2]=1
