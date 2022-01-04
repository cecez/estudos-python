# Arquivos

```python
arquivo = open("palavras.txt", "w") # modo pode ser "r" (read), "a" (append) ou "b" (binário)
arquivo.write("abacate\n")
arquivo.close()

# Por exemplo, o código abaixo cria uma cópia de uma imagem:
logo = open('python-logo.png', 'rb')
data = logo.read()
logo.close()
logo2 = open('python-logo2.png', 'wb')
logo2.write(data)
logo2.close()

arquivo2 = open("palavras.txt", "r") 
linha = arquivo.readline()
arquivo.close()

# sintaxe para abertura de arquivo mais segura
with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)
```