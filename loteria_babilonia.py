
import random

def entrada_usuario(msg):
    """
    Validação de entrada do usuário para garantir que é um número e não uma string.
    """
    while True:
        try:
            numero = int(input(msg))
            return numero
        except ValueError as err:
            print("Entre com um valor válido!")
        
        
sorte = random.randint(1,15)

for i in range(3):
    
    numero = entrada_usuario("Tente um valor entre 1 e 15: ")

    if numero < sorte:
        print("Tente um número maior")

    elif numero > sorte:
        print("Tente um número menor")

    else:
        print("Acertou miserávi!") 
        break

else:
    print(f"Acabaram suas chances! O resultado correto era {sorte}")
    
    