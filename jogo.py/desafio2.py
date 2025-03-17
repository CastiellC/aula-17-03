import random

def escolher_dificuldade():
    print("Escolha a dificuldade:")
    print("1 - Fácil (8 tentativas)")
    print("2 - Médio (5 tentativas)")
    print("3 - Difícil (3 tentativas)")
    escolha = input("Escolha 1, 2 ou 3: ")
    
    if escolha == '1':
        return 8 
    elif escolha == '2':
        return 5 
    elif escolha == '3':
        return 3 
    else:
        print("Opção inválida, escolha 1 por padrão.")
        return 8
    numero_secreto = random.randint(1, 100)

print ("JOGO DA ADIVINHAÇÃO")
print ("tente adivinhar o numero de 1 a 100!")

tentativas = escolher_dificuldade() 
numero_secreto = random.randint(1, 100) 
    
while tentativas > 0:
        print(f"Tentativas restantes: {tentativas}")
        palpite = int(input("Qual o seu palpite? "))
        
        if palpite < numero_secreto:
            print("O número é maior.")
        elif palpite > numero_secreto:
            print("O número é menor.")
        else:
            print("Você acertou! Parabéns!")
            break
        
        tentativas -= 1 
        
        if tentativas == 0:
            print(f"Você perdeu! O número era {numero_secreto}.")