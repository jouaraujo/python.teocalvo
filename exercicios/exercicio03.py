"""
Faça um programa que receba 4 notas de um aluno. 
Retorne a média dessas notas, a menor e a maior nota:

média: x
menor: y
maior: z
"""
#%%
total = 0
notas = []
while total < 4:
    nota = int(input("Entre com uma nota: "))
    notas.append(nota)
    total += 1

print(notas)
notas.sort()

print(f"média: {sum(notas) / len(notas)}")
print(f"menor: {notas[0]}")
print(f"maior: {notas[-1]}")

    
"""
Considere a lista: [120,"python",120.01,"asn",False,[10,20]]

Faça um programa que retorne as seguintes informações:
 -Elemento na posição -1 da lista
 -Elemento na primeira posição da lista
 -O último caractere do segundo elemento da lista
 
Elemento -1: x
primeiro elemento: y
último caractere do segundo elemento: z
"""
#%%
lista = [120,"python",120.01,"asn",False,[10,20]]

print(f"Elemento -1: {lista[-1]}")
print(f"Primeiro elemento: {lista[0]}")
print(f"Último caractere do segundo elemento: {lista[1][-1]}")

"""
Escreva um programa que solicite ao usuário duas
strings e as concatene em uma única String. Em seguida,
exiba a string resultante.
"""
#%%
str_1 = input("Escreva algo: ")
str_2 =input("Escreva algo: ")

str = f"{str_1} {str_2}"

print(str)

"""
Refaça o exercício 2.2 utilizando for e listas para
receber as notas dos alunos
"""

"""
Faça um programa com uma função que recebe
uma frase. Para cada palavra nesta frase, inverta a 
ordem das letras. Exiba o resultado:

Esta é a frase original

aesE é a esarf lanigiro 
"""
#%%
frase = input("Entre com uma frase: ")
print(frase[::-1])

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
lista.sort()
print(f"O maior valor está na posição: {lista[-1]}")
print(f"O menor valor está na posição: {lista[0]}")

"""
Escreva um programa que receba uma lista de
números do usuário e conte quantas vezes um
número específico aparece na lista. Solicite ao
usuário um número e exiba a contagem.
"""

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
