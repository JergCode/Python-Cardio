from art import tprint

import helpers.print_screen as screen
from conversor_functions import convert

OPTIONS = dict({
    1: ('Millas a Kilometros', 'mi_to_km', 'Millas', 'Kilometros'),
    2: ('Millas a Metros', 'mi_to_m', 'Millas', 'Metros'),
    3: ('Millas a Centimetros', 'mi_to_cm', 'Millas', 'Centimetros'),
    4: ('Millas a Yardas', 'mi_to_yd', 'Millas', 'Yardas'),
    5: ('Millas a Pies', 'mi_to_ft', 'Millas', 'Pies'),
    6: ('Millas a Pulgadas', 'mi_to_in', 'Millas', 'Pulgadas'),
    7: ('Kilometros a Millas', 'km_to_mi', 'Kilometros', 'Millas'),
    8: ('Kilmetros a Yardas', 'km_to_yd', 'Kilmetros', 'Yardas'),
    9: ('Kilmetros a Pies', 'km_to_ft', 'Kilmetros', 'Pies'),
    10: ('Kilmetros a Pulgadas', 'km_to_in', 'Kilmetros', 'Pulgadas'),
    11: ('Kilmetros a Metros', 'km_to_m', 'Kilmetros', 'Metros'),
    12: ('Kilmetros a Centrimetos', 'km_to_cm', 'Kilmetros', 'Centrimetos'),
})


def get_unit_messurements(option):
    return OPTIONS.get(option)[2], OPTIONS.get(option)[3]


def welcome():
    screen.clear_screen()
    tprint('Conversor de Unidades', 'standard')
    screen.print_framed_message(['Seleccione el tipo de Conversion que desea realizar', ], 125)


def show_conversion_options():
    print()
    str_options = [f'{str(k)}: {v[0]}' for k, v in OPTIONS.items()]
    screen.print_framed_message(str_options, 125, 'left', 1)
    print()


def ask_for_conversion_option():
    show_conversion_options()
    option = screen.ask_for_option('Opción', len(OPTIONS))
    return option, OPTIONS.get(option)[1]


def ask_for_value(option):
    unit, to_unit = get_unit_messurements(option)
    while True:
        value = input(f'{unit} a convertir: ')
        if value.isnumeric():
            return float(value)
        else:
            print('El valor no es un número valido, intente de nuevo...')


def show_converted_value(option, value, conv_value):
    unit, to_unit = get_unit_messurements(option)
    print(f'{value} {unit} es igual a {conv_value} {to_unit}')


def run():
    while True:
        welcome()
        option, conversion_option = ask_for_conversion_option()
        value = ask_for_value(option)
        conv_value = convert(value, conversion_option)
        show_converted_value(option, value, conv_value)
        print()
        if not screen.ask_to_continue('Desea hacer otra conversión'):
            break


if __name__ == '__main__':
    run()
