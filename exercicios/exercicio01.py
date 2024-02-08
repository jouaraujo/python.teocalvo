"""
Escreva um programa que receba o nome de uma pessoa
e faça uma saudação.

"Olá fulano! Seja Bem vindo!"
"""
#%%
nome = input("Entre com o seu nome: ")
print(f"Olá {nome}! Seja bem vindo!")

"""
Escreva um programa que receba o nome e a idade
de uma pessoa. Depois exiba a mensagem:

"Olá fulano, bom saber que você tem x anos.
Seja bem vindo!"
"""
#%%
nome = input("Entre com o seu nome: ")
idade = int(input("Entre com a sua idade: "))
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
raio = float(input("Entre com o tamanho do raio: "))
perimetro = 2 * 3.14 * raio
area = 3.14 * (raio ** 2)

print(f"Área = {area:.2f}")
print(f"Perímetro = {perimetro:.2f}")


"""
Faça um programa que receba dois valores A e B. Faça a soma
desses dois valores e retorne o resultado:

soma: x.xx
"""
#%%
a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
print(f"soma de {a} com {b} é igual à {a + b}")

"""
Faça um programa que receba dois valores 
A e B. Faça a potência desses dois valores e retorne o resultado

a ^ b = z 
"""
#%%
a = int(input("Digite um número para ser  expoente : "))
b = int(input("Digite qual a potência:"))
print(f"{a} elevado à {b} é igual a {a ** b}")


"""
Faça um programa que receba um número em segundos, converta
 esse número para horas, minutos e segundos. Exemplos:
 
 entrada : 556
 saida : 0:9:16
 
 entrada : 140153
 saida : 38:55:53
"""
# %%
num = int(input("Digite um segundos para serem convertidos em horas, minutos e segundo"))
convert_hora = round(num / 3600)
convert_min = round(num / 60)
convert_sec = round((num / 3600)*100)
print(f"entrada: {num}")
print(f"saida: {convert_hora}:{convert_min}:{convert_sec}")

