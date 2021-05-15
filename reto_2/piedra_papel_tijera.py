from art import *

from helpers.print_screen import clear_screen, ask_to_continue, print_framed_message
from piedra_papel_tijera_functions import play, ask_for_option


def welcome_screen():
    clear_screen()
    print_framed_message(('¡¡¡BIENVENIDO, JUGUEMOS UN POCO A!!!',), 125)
    tprint("PIEDRA PAPEL TIJERA")


def quantity_of_plays_option():
    score_to_win = ask_for_option('Cuantos puntos se necesitan para ganar (1, 2 ... 5)', 5)
    max_games = score_to_win * 2 + 1
    return score_to_win, max_games


def play_against_computer():
    while True:
        answer = input('¿Quieres jugar con la computadora (S/N)? ')
        if answer.upper() == 'S':
            return True
        elif answer.upper() == 'N':
            return False


def show_winner(winner=None):
    print(winner)
    clear_screen()
    if winner:
        tprint('FELICIDADES', 'modular')
        print_framed_message((winner + ' es el ganador del juego', ), 125)
    else:
        tprint('BUEN INTENTO', 'stop')
        print_framed_message(('La computadora ha ganado este juego', ), 125)


def print_winner(winner):
    switch_case = {
        1: lambda: show_winner('Jugador 1'),
        2: lambda: show_winner('Jugador 2'),
        3: lambda: show_winner()
    }

    switch_case.get(winner)()


def run():
    while True:
        welcome_screen()
        games_to_win, max_games = quantity_of_plays_option()
        computer = play_against_computer()
        print(f'\nExcelente entonces gana el que tenga {games_to_win} puntos de {max_games}...')
        print('¡Empecemos!\n')
        winner = play(games_to_win, max_games, computer)
        print_winner(winner)
        if not ask_to_continue('Otro juego'):
            break


if __name__ == '__main__':
    run()
