from art import tprint

import helpers.print_screen as screen


def welcome():
    screen.clear_screen()
    tprint('Rangos Cambiantes', 'standard')
    messages = [
        'Ingresa 3 números: un límite inferior, un límite superior y uno de comparación.',
        ' ',
        'Si tu número de comparación se encuentra en el rango de los dos límites, se imprimirá en la pantalla.'
        ' ',
        'En caso de estar por debajo del inferior o arriba del superior, se mostrará este POR DEBAJO o POR ENCIMA',
        'según sea el caso.',
    ]
    screen.print_framed_message(messages, 108, 'left', 1)
    print()


def ask_for_number(message):
    while True:
        number = input(message)
        if number.isnumeric():
            return float(number)
        else:
            print('El valor ingresado no es numérico, intenta de nuevo...')


def ask_for_ranges():
    lower = ask_for_number('Ingresa el rango inferior: ')
    higher = ask_for_number('Ingresa el rango inferior: ')
    comparison = ask_for_number('Ingresa el rango inferior: ')
    print()
    return lower, higher, comparison


def run_comparison(lower, higher, comparison):
    if comparison < lower:
        print(f'El número {comparison} se encuentra POR DEBAJO del rango {lower}')
    elif comparison > higher:
        print(f'El número {comparison} se encuentra POR ENCIMA del rango {higher}')
    else:
        print(f'El número {comparison} se encuentra DENTRO del rango de {lower} al {higher}')
    print()


def run():
    while True:
        welcome()
        lower, higher, comp = ask_for_ranges()
        run_comparison(lower, higher, comp)
        if not screen.ask_to_continue('Quieres volver a intentarlo'):
            break


if __name__ == '__main__':
    run()