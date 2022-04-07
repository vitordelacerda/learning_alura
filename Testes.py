import random
import time
print('*'*7, 'Vamos brincar de adivinhação?', '*'*7)
time.sleep(1)
print('Estou pensando em um número entre 0 e 10... você consegue adivinhar em qual número estou pensando?')

# Utilizando repetidor "While"
'''tentativas = 1
print('-'*7, f'Tentativa {tentativas}', '-'*7)
num_chute = int(input('Qual número estou pensando? '))
num_certo = random.randint(0,10)

while num_certo != num_chute:
    tentativas = tentativas + 1
    print(f'Você chutou {num_chute} e eu pensei no número {num_certo}. Tente outra vez!')
    print('-'*7, f'Tentativa {tentativas}', '-'*7)
    num_chute = int(input('Qual número estou pensando? '))
    num_certo = random.randint(0,10)

print(f'Você chutou {num_chute} e eu pensei no mesmo número. Você acertou com {tentativas} tentativas')'''


# Utilizando repetidor "For"

total_tentativas = 15

for rodada in range (1, total_tentativas + 1):
    print('-'*7, f'Tentativa {rodada} de {total_tentativas}', '-'*7)
    num_certo = random.randint(0,10)
    print('Qual numero estou pensando?')
    time.sleep(1)
    num_chute = int(input('Você está pensando no número... '))
    print('Hmmm, bom chute... será que você acertou?')
    if num_chute != num_certo:
        print(f'Você chutou {num_chute} e eu pensei no número {num_certo}. Tente outra vez!')

    elif num_chute == num_certo:
        print(f'Você chutou {num_chute} e eu pensei no mesmo número. Você acertou com {rodada} tentativas!')
        break
    
    
    