from art import *

from helpers.print_screen import clear_screen, ask_to_continue
from triangle_functions import calculate_triangle_area, calculate_type


def _print_welcome():
    clear_screen()
    tprint('TRIANGLE     AREA')
    print('+' + '-' * 98 + '+')
    print('|' + 'CALCULADORA DE TRIANGULOS'.center(98, ' ') + '|')
    print('+' + '-' * 98 + '+')
    print('| Hola bienvenido a su calculadora de área de triangulos'.ljust(99, ' ') + '|')
    print('| Para poder ayudarle necesitaré de algunos datos '.ljust(99, ' ') + '|')
    print('+' + '-' * 98 + '+')
    print()


def _ask_for_arguments():
    b = 0.0
    h = 0.0
    while True:
        try:
            b = float(input('¿Cuál es la base del triangulo? '))
            h = float(input('¿Cuál es la altura del triangulo? '))
            area = calculate_triangle_area(b, h)
            print(f'\nEl área de su triangulo es: {area}\n')
            break
        except ValueError as error:
            if 'could not convert' in str(error):
                print('Valor no valido, favor de volver a intentarlo\n')
            else:
                print(error)
            continue

    return b, h


def _ask_for_type_of_triangle(base, height):
    while True:
        option = input('¿Desea saber que tipo de triángulo es (Y/N)? ')
        if option.upper() == 'Y':
            try:
                print('\nPara esto necesito saber la lóngitud de sus otros lados')
                side_a = float(input('Lado A: '))
                side_c = float(input('Lado C: '))
                tipo = calculate_type(base, side_a, side_c, height)
                print(f'El triángulo es {tipo}')
                break
            except ValueError as ex:
                print(ex)
                continue
        elif option.upper() == 'N':
            break

        print('Opción no valida... ')
        continue


def run():
    keep_going = True
    while keep_going:
        _print_welcome()
        base, height = _ask_for_arguments()
        _ask_for_type_of_triangle(base, height)
        keep_going = ask_to_continue('Le gustaría calcular otra área')


if __name__ == '__main__':
    run()
