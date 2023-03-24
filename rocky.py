import random
choices = ['rock', 'paper', 'scissors']
player_score = 0
cpu_score = 0
rounds = 5

def get_cpu_choices():
    return choices[int(random.randrange(0,3))]

def play_round(player, cpu):
    if player == cpu:
        print(f'tie - both choose {player}')
    elif player == 'rock' and cpu == 'scissors' or player == 'paper' and cpu == 'rock' or player == 'scissors' and cpu == 'paper':
        print(f'player wins - {player} beats {cpu}')
    else:
        print(f'player lose - {cpu} beats {player}')
    
play_round(str(input('Rock, paper or scissors? ')), str(get_cpu_choices()))