import random
from helpers.print_screen import print_framed_message
from options import OPTIONS, parse_option


def select_option():
    print('Selecciona una de las opciónes: \n')
    for option in OPTIONS:
        print(f'{option.get_option()} : {option.name}'.ljust(20))
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

    input()

    if p1_wins > p2_wins:
        return 1
    elif not against_computer:
        return 2
    else:
        return 3


def _compute_winner(p1_option, p2_option, against_computer):
    if p1_option == p2_option:
        print(f'\nJuagdor 1:({p1_option.name}) no le gana a {"Computadora" if against_computer else "Jugador 2"}:({p2_option.name})\n')
        return 0
    if p1_option.wins_against_options(p2_option):
        _print_winner_of_game(p1_option, player_1_won=True, against_computer=against_computer)
        return -1
    else:
        _print_winner_of_game(p2_option, player_1_won=False, against_computer=against_computer)
        return 1


def _print_winner_of_game(winning_option, player_1_won, against_computer):
    option = winning_option.value[0]
    if player_1_won:
        winner = 'Jugador 1'
        loser = 'Computadora' if against_computer else 'Jugador 2'
    else:
        loser = 'Jugador 1'
        winner = 'Computadora' if against_computer else 'Jugador 2'

    messages = dict({
        1: f'\nPIEDRA({winner}) destruye a TIJERAS({loser})\n',
        2: f'\nPAPEL({winner}) envuelve a PIEDRA({loser})\n',
        3: f'\nTIJERA ({winner}) corta a PAPEL({loser})\n',
    })
    print(messages.get(option))


def ask_for_option(message, max_options):
    while True:
        option = input(f'¿{message}? ')
        if option.isnumeric() and 0 <= int(option) <= max_options:
            return int(option)
        else:
            print('El valor no es válido, ingrese un número por favor')


def ask_for_players_option(against_computer):
    p1_option = parse_option(ask_for_option('Opción del Jugador 1', 3))
    if not against_computer:
        p2_option = parse_option(ask_for_option('Opción del Jugador 2', 3))
        print()
    else:
        p2_option = parse_option(random.randint(1, 3))
    return p1_option, p2_option
