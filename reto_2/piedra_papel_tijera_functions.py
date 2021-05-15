import random
from helpers.print_screen import print_framed_message
from options import OPTIONS

def select_option():
    print('Selecciona una de las opciónes: \n')
    for option in OPTIONS:
        print(f'{option.value} : {option.name}'.ljust(20))
    print()


def play(games_to_win, max_games, against_computer=False):
    games = 0
    p1_wins = 0
    p2_wins = 0

    while games < max_games and p1_wins < games_to_win and p2_wins < games_to_win:
        print_framed_message(
            ('SCORE:', f'Juegos jugados: {games}',
             f'Jugador 1: {p1_wins} --- {"Computadora: " if against_computer else "Jugador 2: "}{p2_wins}'), 125)

        select_option()
        p1_option, p2_option = ask_for_players_option(against_computer)
        score = _compute_winner(p1_option, p2_option, against_computer)
        if score == -1:
            p1_wins += 1
            games += 1
        elif score == 0:
            continue
        elif score == 1:
            p2_wins += 1
            games += 1

    if p1_wins > p2_wins:
        return 1
    elif not against_computer:
        return 2
    else:
        return 3

def _compute_winner(p1_option, p2_option, against_computer):
    if p1_option == p2_option:
        print(f'\nJuagdor 1:({p1_option.name}) no le gana a Juagdor 2:({p2_option.name})\n')
        return 0
    if p1_option is OPTIONS.PIEDRA and p2_option is OPTIONS.PAPEL:
        _print_winner_of_game(2, player_1_won=False, against_computer=against_computer)
        return 1
    if p1_option is OPTIONS.PIEDRA and p2_option is OPTIONS.TIJERA:
        _print_winner_of_game(1, player_1_won=True, against_computer=against_computer)
        return -1
    if p1_option is OPTIONS.PAPEL and p2_option is OPTIONS.PIEDRA:
        _print_winner_of_game(2, player_1_won=True, against_computer=against_computer)
        return -1
    if p1_option is OPTIONS.PAPEL and p2_option is OPTIONS.TIJERA:
        _print_winner_of_game(3, player_1_won=False, against_computer=against_computer)
        return 1
    if p1_option is OPTIONS.TIJERA and p2_option is OPTIONS.PIEDRA:
        _print_winner_of_game(3, player_1_won=True, against_computer=against_computer)
        return -1
    if p1_option is OPTIONS.TIJERA and p2_option is OPTIONS.PAPEL:
        _print_winner_of_game(2, player_1_won=False, against_computer=against_computer)
        return 1


def _print_winner_of_game(winning_option, player_1_won, against_computer):
    if player_1_won:
        winner = 'Jugador 1'
        loser = 'Computadora' if against_computer else 'Jugador 2'
    else:
        loser = 'Jugador 1'
        winner = 'Computadora' if against_computer else 'Jugador 2'

    messages = dict({
        1: f'PIEDRA({winner}) destruye a TIJERAS({loser})',
        2: f'PAPEL({winner}) envuelve a PIEDRA({loser})',
        3: f'TIJERA ({winner}) corta a PAPEL({loser})',
    })

    print(messages.get(winning_option))


def ask_for_option(message, max_options):
    while True:
        option = input(f'¿{message}? ')
        if option.isnumeric() and 0 <= int(option) <= max_options:
            return int(option)
        else:
            print('El valor no es válido, ingrese un número por favor')


def ask_for_players_option(against_computer):
    p1_option = OPTIONS(ask_for_option('Opción del Jugador 1', 3))
    if not against_computer:
        p2_option = OPTIONS(ask_for_option('Opción del Jugador 2', 3))
        print()
    else:
        p2_option = OPTIONS(random.randint(1, 3))
    return p1_option, p2_option
