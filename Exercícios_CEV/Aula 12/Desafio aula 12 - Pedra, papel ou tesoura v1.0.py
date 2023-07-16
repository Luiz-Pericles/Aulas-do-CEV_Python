'''Programe o famoso jogo pedra, papel ou tesoura!'''
import random
print('\033[;30;48m==\033[m'*24)
print('\033[1;32;40mBem-vindo(a) ao Pedra, Papel ou Tesoura!\033[m')
print('\033[1;32;40mEu sou a máquina e irei jogar com você.\033[m')
print('\033[;30;48m==\033[m'*24)

user_points = 0
computer_points = 0
options = ['R', 'P', 'S']

while True:
    user_choice = str(input('Digite: R(Pedra);P(Papel); S(Tesoura); Q (Exit):  ').upper())

    if user_choice == 'Q':
        break
    if user_choice not in options:
        continue


    computer_choice = random.randint(0,2)
    #0 : R ,1 : P, 2 : S.
    computer_option = options[computer_choice]

    if user_choice == computer_option:
        print(f'Empate! A máquina escolheu: {computer_option}')
    elif user_choice == 'R' and computer_option == 'S':
        print(f'Você ganhou! A máquina escolheu: {computer_option}')
        user_points = user_points + 1
    elif user_choice == 'P' and computer_option == 'R':
        print(f'Você ganhou! A máquina escolheu: {computer_option}')
        user_points = user_points + 1
    elif user_choice == 'S' and computer_option == 'P':
        print(f'Você ganhou! A máquina escolheu: {computer_option}')
        user_points = user_points + 1

    else:
        print(f'A máquina ganhou! Ela escolheu: {computer_option}')
        computer_points = computer_points + 1

print(f'\nSua pontuação foi: {user_points}')
print(f'A pontuação da máquina foi: {computer_points}')
if user_points > computer_points:
    print('Você venceu a máquina, PARABÉNS!')
elif user_points == computer_points:
    print('Você empatou com a máquina, FOI POR POUCO!')
else:
    print('Você perdeu para a máquina, BOA SORTE NA PRÓXIMA!')


print('\nGoodbye!')








