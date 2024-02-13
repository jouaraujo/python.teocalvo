sorte = 7

for i in range(3):
    numero = int(input("Entre com um número da sorte entre 1 e 15: "))

    if numero < sorte:
        print("Tente um número maior")

    elif numero > sorte:
        print("Tente um número menor")

    else:
        print("Acertou miserávi!") 
        break

else:
    print("Acabaram suas chances!")
    