"""
Escreva um programa que receba o nome de uma pessoa
e faça uma saudação.

"Olá fulano! Seja Bem vindo!"
"""
#%%
nome = input("Digite seu nome: ")
print(f"Olá {nome}! Seja bem vindo!")

"""
Escreva um programa que receba o nome e a idade
de uma pessoa. Depois exiba a mensagem:

"Olá fulano, bom saber que você tem x anos.
Seja bem vindo!"
"""
#%%
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"Olá {nome}, bom saber que você tem {idade} anos.")
print("Seja bem vindo!")

"""
Faça um programa que receba o raio de 
uma circunferência em centímetros. Retorne
para o usuário qual é a área e perímetro desta
circunferência no seguinte formato.

"Área = x.xx"
"Perímetro = y.yy"
"""
#%%
import math as m

r = float(input("Digite o raio do circulo: "))
perimetro = 2 * m.pi * r
area = m.pi * (r ** 2)

print(f"Área = {area}:")
print(f"Perímetro = {perimetro}")


"""
Faça um programa que receba dois valores A e B. Faça a soma
desses dois valores e retorne o resultado:

soma: x.xx
"""

"""
Faça um programa que receba dois valores 
A e B. Faça a potência desses dois valores e retorne o resultado

a ^ b = z 
"""

"""
Faça um programa que receba um número em segundos, converta
 esse número para horas, minutos e segundos. Exemplos:
 
 entrada : 556
 saida : 0:9:16
 
 entrada : 140153
 saida : 38:55:53
"""