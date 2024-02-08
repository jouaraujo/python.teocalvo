#%%
nome = "Téo Calvo"

j = 1
for i in nome:
    print(f"Elemento {j}: {i}")
    j += 1
    
#%%
for i in range(1, 11):
    print(i)

#%%
i = int(input("Entre com o valor mínimo:"))
j = int(input("Entre com o valor máximo: "))

for i in range(i, j+1):
    print(i)