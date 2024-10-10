import random

repeat = True

while repeat:
    print("O que deseja:")
    print("1_ Acertar o número")
    print("2_ Sair")
    
    opcao = input("> ")
    
    if opcao == "1":
        print("Advinhe o número de 0 a 1999")
        num = random.randint(0, 1999)
        
        repeat2 = True
        
        while repeat2: 
            n = int(input("Digite um número\n"))
            if n == num:
                print("\n\nVocê acertou o número!!!")
                repeat2 = False
            elif n < num:
                print("O número é maior")
            elif n > num:
                print("O número é menor")
    elif opcao == "2":
        repeat = False
    else:
        print("Opção inválida")