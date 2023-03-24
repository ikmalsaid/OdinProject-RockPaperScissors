import random

choices = ['rock', 'paper', 'scissors']
player_score = 0
cpu_score = 0
rounds = 0
question = f'Round {rounds + 1} of 5 - Rock, paper or scissors? '

def get_cpu_choices():
    return choices[random.randint(0, 2)]

def play_round(player, cpu, rounds, player_score, cpu_score):
    rounds += 1
    if player == cpu:
        print(f'Tie - both chose {player}')
    elif player == 'rock' and cpu == 'scissors' or player == 'paper' and cpu == 'rock' or player == 'scissors' and cpu == 'paper':
        player_score += 1
        print(f'Player wins - {player} beats {cpu}')
    else:
        cpu_score += 1
        print(f'CPU wins - {cpu} beats {player}')
    return rounds, player_score, cpu_score

while rounds < 5:
    player_choice = input(question)
    cpu_choice = get_cpu_choices()
    rounds, player_score, cpu_score = play_round(player_choice, cpu_choice, rounds, player_score, cpu_score)
    question = f'Round {rounds + 1} of 5 - Rock, paper or scissors? '

if player_score > cpu_score:
    print(f'Player wins! {player_score} beats {cpu_score}')
elif cpu_score > player_score:
    print(f'CPU wins! {cpu_score} beats {player_score}')
else:
    print(f'Tie - both have {player_score} points')
