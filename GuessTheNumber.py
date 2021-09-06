from random import randint
import os

def verifica(chute, n):
    tentativa = 1
    chutes = []
    while chute != n:
        if chute < n:
            tentativa += 1
            chutes.append(chute)
            print(f'Tentativa número: {tentativa:.0f}')
            print('Chutes: ',chutes)
            chute = int(input('\nTente um valor maior: '))
            os.system('cls' if os.name == 'nt' else 'clear')
        if chute > n:
            tentativa += 1
            chutes.append(chute)
            print(f'Tentativa número:{tentativa:.0f}')
            print('Chutes: ',chutes)
            chute = int(input('\nTente um valor menor: '))
            os.system('cls' if os.name == 'nt' else 'clear')
    if chute == n:
        print(f'Acertou em {tentativa:.0f} tentativas!')
        chutes = []
        tentativa = 1

def jogar_():
    jogar = input("Deseja jogar novamente?\n\nInsira 'sim' ou 'não': ")
    os.system('cls' if os.name == 'nt' else 'clear')
    return jogar

def inicio(tentativa):
    print(f'Tentativa número:{tentativa:.0f}')
    chute = int(input('\nChute um valor: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    return chute

jogar = 'sim'
tentativa = 1
chutes = []

while jogar == 'sim':
    print('Nível de dificuldade:')
    print('\n1)100 possibilidades')
    print('2)500 possibilidades')
    print('3)1.000 possibilidades')
    print('4)100.000 possibilidades')
    print('5)1.000.000 possibilidades')

    dificuldade = int(input('\nInsira o número da opção: '))
    os.system('cls' if os.name == 'nt' else 'clear')

    if dificuldade == 1: 
        n = randint(1,100)
        chute = inicio(tentativa)
        verifica(chute, n)
        
    if dificuldade == 2:
        n = randint(1,500)
        chute = inicio(tentativa)
        verifica(chute, n)

    if dificuldade == 3:
        n = randint(1,1000)
        chute = inicio(tentativa)
        verifica(chute, n)

    if dificuldade == 4:
        n = randint(1,100000)
        chute = inicio(tentativa)
        verifica(chute, n)

    if dificuldade == 5:
        n = randint(1,1000000)
        chute = inicio(tentativa)
        verifica(chute, n)
        
    jogar = jogar_()

input('Até a próxima!')
