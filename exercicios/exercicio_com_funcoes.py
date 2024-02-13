"""
Faça um programa que receba um número e retorne seu fatorial.
"""
#%%
# Recursão
# def fat_rec(x):
#     if x == 0:
#         return 1
#     else:
#         return x * fat_rec(x-1)

def fat(x):
    total = 1
    for i in range(1,x+1):
        total *= i
    return total

n1 = int(input("Entre com um número: "))
n2 = int(input("Entre com um número: "))

fat_n1 = fat(n1)
fat_n2 = fat(n2)

print(f"{n1}! = {fat_n1}")
print(f"{n2}! = {fat_n2}")


#%%
"""
Função para par e ímpar
"""

def par_impar(x):
    if x % 2 == 0:
        return "par"
    else:
        return "impar"
    
n1 = int(input("Entre com um número: "))
n2 = int(input("Entre com um número: "))

print(f"O número {n1} é {par_impar(n1)}!")
print(f"O número {n2} é {par_impar(n2)}!")
