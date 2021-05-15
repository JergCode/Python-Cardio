import os
import platform


def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def ask_to_continue(message):
    answer = input(f'¿{message} (Y/N)? ')
    if answer.upper() == 'Y':
        return True
    else:
        return False


def print_framed_message(messages, width):
    if not isinstance(messages, tuple):
        raise ValueError('Favor de envolver tu mensaje en una tupla')

    print('+' + '-' * (width - 2) + '+')
    for message in messages:
        print('|' + message.center(width - 2, ' ') + '|')
    print('+' + '-' * (width - 2) + '+')
