# List Comprehension
Formas de criar uma lista a partir de outra, de forma mais elegante e sem gerar efeitos colaterais.

````python
inteiros = [1,3,4,5,7,8]
# para cada inteiro da lista inteiros, cria o quadrado na lista quadrados
quadrados = [n*n for n in inteiros] # list comprehension

frutas = ["maçã", "banana", "laranja", "melancia"]
lista = [fruta.upper() for fruta in frutas]

inteiros = [1,3,4,5,7,8,9]
pares = [i for i in inteiros if i % 2 == 0]
````