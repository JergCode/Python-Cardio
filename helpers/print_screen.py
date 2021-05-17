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


def print_framed_message(messages, width, alignment='center', padding=0):
    if not (isinstance(messages, list) or isinstance(messages, str)):
        raise ValueError('Favor de enviar solo Strings o un Tuple con Strings')

    for message in messages:
        if not isinstance(message, str):
            raise ValueError('Favor de enviar solo Strings o un Tuple con Strings')

    print('+' + '-' * (width - 2) + '+')
    if isinstance(messages, str):
        print('|' + align_message(messages, width, alignment, padding) + '|')
    else:
        for message in messages:
            print('|' + align_message(message, width, alignment, padding) + '|')
    print('+' + '-' * (width - 2) + '+')


def align_message(message, width, alignment, padding):
    if alignment == 'center':
        return message.center(width - 2, ' ')
    if alignment == 'left':
        return ' ' * padding + message.ljust(width - (2 + padding), ' ')
    if alignment == 'right':
        return message.rjust(width - (2 + padding), ' ') + ' ' * padding
    return message


def ask_for_option(message, max_options):
    while True:
        option = input(f'¿{message}? ')
        if option.isnumeric() and 0 <= int(option) <= max_options:
            return int(option)
        else:
            print('El valor no es válido, ingrese un número por favor')