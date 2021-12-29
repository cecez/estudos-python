# Aula 3

## Tuplas (tuple)
Lista de dados **imutável**.

Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).

```python
valores = ("D", "S", "T", "Q", "Q", "S", "S")

type(valores)
# >>> <class 'tuple'>

# converter lista para tupla
lista = [1,2,3,4,5]
tupla = tuple(lista)
print(tupla)
# >>> (1, 2, 3, 4, 5)

# converter tupla para lista
lista = list(tupla)
```

Documentação: https://docs.python.org/3/library/stdtypes.html#tuple

## Conjunto (set)
Lista de dados que **não se repetem**.

**Não possui índice. Não é ordenado.**

```python
valores = {1,2,3,4,5}

valores.add(10)
```

## Dicionário (dictionary)
Lista de dados chave-valor. (Não é um set).

```python
valores = {'Cezar': 35, 'Ana': 39, 'João Pedro': 6}

print(valores['Cezar'])
# >>> 35


```