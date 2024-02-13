"""
Faça um programa que receba 4 notas de um aluno. 
Retorne a média dessas notas, a menor e a maior nota:

média: x
menor: y
maior: z
"""
#%%
n1 = float(input("Entre com a nota 1: "))
n2 = float(input("Entre com a nota 2: "))
n3 = float(input("Entre com a nota 3: "))
n4 = float(input("Entre com a nota 4: "))

notas = [n1,n2,n3,n4]

media = sum(notas) / len(notas)
minimo = min(notas)
maximo = max(notas)

print(f"Média: {media}")
print(f"menor: {minimo}")
print(f"maior: {maximo}")

    
"""
Considere a lista: [120,"python",120.01,"asw",False,[10,20]]

Faça um programa que retorne as seguintes informações:
 -Elemento na posição -1 da lista
 -Elemento na primeira posição da lista
 -O último caractere do segundo elemento da lista
 
Elemento -1: x
primeiro elemento: y
último caractere do segundo elemento: z
"""
#%%
lista = [120,"python",120.01,"asw",False,[10,20]]

print(f"Elemento -1: {lista[-1]}")
print(f"Primeiro elemento: {lista[0]}")
print(f"Último caractere do segundo elemento: {lista[1][-1]}")

"""
Escreva um programa que solicite ao usuário duas
strings e as concatene em uma única String. Em seguida,
exiba a string resultante.
"""
#%%
s1 = input("Entre com uma frase: ")
s2 = input("Entre com outra frase: ")

string_final = s1 + s2
print(string_final)

"""
Refaça o exercício 2.2 utilizando for e listas para
receber as notas dos alunos
"""
#%%
# notas = []

# for i in range(4):
#     n = float(input(f"Entre com a nota {i+1}: "))
#     notas.append(n)

notas = [float(input(f"Entre com a nota {i+1}: ")) for i in range(4)]
    
media = sum(notas) / len(notas)
minimo = min(notas)
maximo = max(notas)

print(f"Média: {media}")
print(f"Mínimo: {minimo}")
print(f"máximo: {maximo}")


"""
Faça um programa com uma função que recebe
uma frase. Para cada palavra nesta frase, inverta a 
ordem das letras. Exiba o resultado:

Esta é a frase original

aesE é a esarf lanigiro 
"""
#%%
frase = input("Entre com uma frase: ")
#print(frase[::-1])
texto = ""
for palavra in frase.split():
    texto = texto + palavra[::-1] + " "

print(texto)

### OUTRA VERSÃO

frase_invertida = []
for palavra in frase.split():
    frase_invertida.append(palavra[::-1])

print(" ".join(frase_invertida))

"""
Considere a seguinte lista:
[123,435,987,1984,2,19,423,-178,320]

Faça um programa que retorne a posição do 
menor e do maior valor encontrado:

O maior valor está na posição x
O menor valore está na posição y
"""
#%%
lista = [123,435,987,1984,2,19,423,-178,320]

menor = min(lista)
maior = max(lista)

menor_index = lista.index(menor)
maior_index = lista.index(maior)

print(f'O menor valor está na posição: {menor_index}')
print(f'O maior valor está na posição: {maior_index}')

"""
Escreva um programa que receba uma lista de
números do usuário e conte quantas vezes um
número específico aparece na lista. Solicite ao
usuário um número e exiba a contagem.
"""
#%%
numeros = []

while True:
    entrada = input("Entre com um número: ")
    
    if entrada == "":
        break
    
    numeros.append(int(entrada))
    
numero_check = input("Entre com um número para checar a quantidade: ")

total = 0
for i in numeros:
    if i == numero_check:
        total += 1
    
print(f"O número {numero_check} aparece {total} vezes. Ou {numeros.count(numero_check)}")
pritn(f"Ou {numeros.count(numero_check)}")
"""
Escreva um programa que socilite ao usuário uma palavra e verifique se
a palavra é um palíndromo (ou seja, é a mesma palavra quando lida de 
trás para frente).
"""
#%%
palavra = input("Entre com uma palavra: ")

if palavra.lower() == palavra[::-1].lower():
    print(f"A palavra {palavra} é palíndromo!")

else:
    print(f"A palavra {palavra} não é palíndromo!")
# %%
