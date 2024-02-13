"""
Escreva um programa que crie um dicionário com nomes
de frutas como chaves e seus respectivos preços como
valores. Solicite ao usuário o nome de uma fruta e 
exiba o preço correspondente.

maçã: R$1,50   pera: R$1,25  goiaba: R$2,15

banana: R$2,75  laranja: R$0,65  abacaxi: R$3,20

Uva: R$1,90  limão: R$1,25  jaca: R$5,80
"""
#%%

frutas ={
    "maçã": "1.50", 
    "pera": "1.25",  
    "goiaba": "2.15",
    "banana": "2.75",  
    "laranja": "0.65",  
    "abacaxi": "3.20",
    "uva": "1.90",  
    "limão": "1.25", 
    "jaca": "5.80"
}

fruta = input("Entre com o nome de uma fruta: ")

if fruta in frutas.keys():
    preco = frutas[fruta]
    print(f"A fruta {fruta} custa R${preco}.")

else:
    print(f"A fruta {fruta} não foi encontrada.")