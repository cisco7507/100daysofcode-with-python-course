import sys

# sys.path.append(".")
from rps import Roll, Player


def print_header():
    print('----------------------------------------')
    print('--------- Rock, Paper, Scissors --------')
    print('----------------------------------------')


def get_player_name():
    try:
        player = input('>>>> Enter your name: ')
    except (EOFError, KeyboardInterrupt):
        print(f'Thanks for playing!, Bye')
        exit(0)
    return player


def get_player_choice():
    try:
        while True:
            choice = input(">>>> Select [R]ock, [P]aper, [S]cissors or [A]bort to exit game: ")

            choice_dict = {
                'r': 'rock',
                'p': 'paper',
                's': 'scissors',
                'a': 'abort'
            }

            if choice_dict.get(choice.lower()) == 'abort':
                print('Thanks for playing')
                exit(0)

            elif choice_dict.get(choice.lower()):
                return choice_dict.get(choice.lower())

            else:
                print(f'Wrong entry, please select [R], [P], [S] for playing or [A] to abort and exit: ')

    except (EOFError, KeyboardInterrupt):
        print(f'Thanks for playing!, Bye')
        exit(0)


if __name__ == '__main__':
    print_header()
    player = get_player_name()

    player_a_name = Player(player).name
    player_b_name = Player('computer').name
    score = {player_a_name: 0, 'computer': 0}

    while True:
        for game in range(3):
            player_a_choice = get_player_choice()
            player_b_choice = Roll().name()
            if Roll(player_a_choice).win() == player_b_choice:
                print(f"{player_a_name} picked: {player_a_choice} which beats {player_b_name}'s {player_b_choice}")
                score[player_a_name] += 1
            elif Roll(player_b_choice).win() == player_a_choice:
                print(f"{player_b_name} picked: {player_b_choice} which beats {player_a_name}'s {player_a_choice}")
                score[player_b_name] += 1
            else:
                print(
                    f'{player_a_name} picked: {player_a_choice}, {player_b_name} picked: {player_b_choice} you are tied!')

        if score[player_a_name] > score['computer']:
            print(
                f'Winner: {player_a_name}, Score: {player_a_name}: {score[player_a_name]}, {player_b_name}: {score[player_b_name]}')
            score = {player_a_name: 0, 'computer': 0}
        elif score[player_a_name] < score['computer']:
            print(
                f'Winner: {player_b_name}, Score: {player_a_name}: {score[player_a_name]}, {player_b_name}: {score[player_b_name]}')
            score = {player_a_name: 0, 'computer': 0}
        else:
            print(f'You are tied, Score: {player_a_name}: {score[player_a_name]}, {player_b_name}: {score[player_b_name]}')
            score = {player_a_name: 0, 'computer': 0}
