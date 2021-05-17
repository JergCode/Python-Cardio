from art import tprint

import helpers.print_screen as screen
from calculation import calculate_volume

OPTIONS = dict({
    1: ('Esfera', ('Radio',)),
    2: ('Cilindro', ('Radio', 'Altura')),
    3: ('Cubo', ('Lado',)),
    4: ('Prisma Triangular', ('Lado 1', 'Lado 2', 'Lado 3', 'Altura')),
    5: ('Ortoedro', ('Lado 1', 'Lado 2', 'Altura')),
})


def welcome():
    screen.clear_screen()
    tprint('Calculadora de Volumen', 'standard')
    screen.print_framed_message(['Seleccione el tipo de Conversion que desea realizar', ], 135)


def print_options():
    print()
    str_options = [f'{str(k)}: {v[0]}' for k, v in OPTIONS.items()]
    screen.print_framed_message(str_options, 135, 'left', 1)
    print()


def get_figure_requirements(option):
    return OPTIONS.get(option)[0], OPTIONS.get(option)[1]


def ask_for_requirement(req):
    while True:
        requirement = input(f'{req}: ')
        if requirement.isnumeric():
            return float(requirement)
        print('El valor ingresado no es númerico, favor de intentar de nuevo...')


def select_option():
    return screen.ask_for_option('Seleccione la figura cuyo volumen desea calcular', len(OPTIONS))


def ask_for_requirements(option):
    figure, requirements = get_figure_requirements(option)
    print(f'Para obtener el volumen de{" la " + figure if figure.startswith("E") else "l " + figure} necesito: \n')
    requirements_values = [
        ask_for_requirement(req) for req in requirements
    ]
    return figure, requirements_values


def get_calculated_volume(figure, requirements):
    volume = calculate_volume(figure, requirements)
    screen.print_framed_message(
        f'El volumén de{" la " + figure if figure.startswith("E") else "l " + figure} es: {volume}', 135, 'left', 1)


def run():
    while True:
        welcome()
        print_options()
        option = select_option()
        figure, requirements = ask_for_requirements(option)
        get_calculated_volume(figure, requirements)
        if not screen.ask_to_continue('Desea calcular otro volumen'):
            break


if __name__ == '__main__':
    run()
