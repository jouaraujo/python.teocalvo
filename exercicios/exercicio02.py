"""
Escreva um programa que solicite ao usuário um número e exiba a tabuada
desse número de 1 a 10
"""
#%%
numero = int(input("Entre com um número:"))

for i in range(1, 11):
    res = numero * i
    txt = f"{numero:2} x {i:2} = {res}"
    print(txt)

"""
Faça um programa que receba um número e retorne seu fatorial
"""
#%%
numero = int(input("Entre com um número: "))

fatorial = 1
for i in range(2, numero+1):
    fatorial *= i
    
print(fatorial)

"""
Escreva um programa que exiba os números de 1 a 100. Caso o número seja
divisível por 3, exiba "Fizz" no seu lugar, e para múltiplos de 5 exiba
"Buzz". Caso seja divisível por ambos, exiba "FizzBuzz"
"""
#%%
for i in range(1, 101):
    
    msg = ""
    if i % 3 == 0:
        msg = msg + "Fizz"
    
    if i % 5 == 0:
        msg = msg + "Buzz"
    
    if msg == "":
        msg = i 
    
    print(msg)

"""
Faça um programa que receba um número. Este número corresponde a uma posição
na sequência Fibonacci:0, 1, 1, 2, 3, 5,...

Exiba o número da sequência cuja posição foi informada:
"A posição x corresponde ao número y"
"""
#%%
numero = int(input("Entre com um número correspondente à posição Fibonacci."))

fib_0 = 0
fib_1 = 1

i = 1
while i < numero:
    fib_n = fib_1 + fib_0
    fib_0 = fib_1
    fib_1 = fib_n
    i += 1
    
print(f"A posição {numero} corresponde ao número {fib_0}")

"""
Faça um programa que receba um número. Verifique se este número é primo ou não,
e retorne o resultado:

"O número x é primo"
ou 
"O número x não é primo"
"""
#%%
numero = int(input("Entre com um número: "))

check = False
for i in range(2, numero):
    if numero % i == 0:
        check = True
        break

if check:
    print(f"O número {numero} não é primo!")

else:
    print(f"O número {numero} é primo!")

#%%
numero = int(input("Entre com um número: "))

check = False
for i in range(2, numero):
    if numero % i == 0:
        print(f"O número {numero} não é primo!")
        check = True
        break

else:
    print(f"O número {numero} é primo!")

"""
Faça um programa que receba um número. 
Verifique se o número informado é par ou ímpar.
Exiba o resultado da seguinte maneira:

"O número x é impar"
ou
"O número x é par"
"""
#%%
numero = int(input("Entre com um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par!")
else:
    print(f"O numero {numero} é impar")

"""
Faça um programa  que receba o nome e a idade de uma pessoa

Caso essa pessoa tenha menos de 18 anos, exiba o aviso:
"Fulano, você não pode dirigir nem beber"

Para as pessoas entre 18 e 65 anos, exiba o aviso:
"Fulano, bebida liberada! Só não vale dirigir!"

Para as pessoas com mais  de 65 anos, exiba o aviso:
"Fulano, beba com muita moderação!"
"""
#%%
nome = input("Entre com seu nome: ")
idade = int(input("Entre com sua idade: "))

if idade < 18:
    print(f"{nome}, você não pode dirigir, nem beber")

elif idade <= 65:
    print(f"{nome}, babida liberada! só não vale dirigir!")

else:
    print(f"{nome}, beba com muita moderação!")