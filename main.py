import random
from time import sleep

print('''
============================================
      Bem Vindo ao jogo de adivinhação
============================================
''')
sleep(0.5)
print('Você terá 5 chances para acertar o número entre 0 e 100 que será sorteado')
sleep(0.5)
print('Boa sorte!!!\n')


numero_sorteado = random.randint(0, 100)
chances = 1

print(numero_sorteado)
while (chances <= 5):
    try:
        sleep(0.5)

        print(f'Chance {chances} de 5')
        chute = int(input('Chute um número => '))

        sleep(0.5)

        if (chute == numero_sorteado):
            print('Você acertou!!!')
            break
        elif (chute < numero_sorteado):
            print('Você chutou um número menor que o sorteado pelo sistema\n')
        elif (chute > numero_sorteado):
            print('Você chutou um número maior que o sorteado pelo sistema\n')
        
        if chances == 5 and chute != numero_sorteado:
            sleep(0.5)
            print(f'Suas chances acabaram')
            sleep(0.5)
            print('mais sorte na proxima vez!')
            sleep(0.5)
            while True:
                recomecar = input('\nRecomeçar? s/n ')
                if recomecar == 's':
                    chances = 0
                    break
                elif recomecar == 'n':
                    break
                else:
                    print('Valor inválido')
        if chances == 5 and recomecar == 'n':
            break     

        chances += 1 
    except:
        print('Valor inválido!!\n')
