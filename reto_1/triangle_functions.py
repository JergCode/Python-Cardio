import math

from numpy import isclose


def calculate_triangle_area(base, height):
    return (base * height) / 2


def _calculate_herons_area(side_a, side_b, side_c):
    s = _get_semiperimeter(side_a, side_b, side_c)
    return (s * (s - side_a) * (s - side_b) * (s - side_c)) ** (1 / 2)


def _get_semiperimeter(side_a, side_b, side_c):
    return (side_a + side_b + side_c) / 2


def _get_hypotenuse(base, height):
    return (height ** 2 + base ** 2) ** (1 / 2)


def _get_side(side_a, hypotenuse):
    return (hypotenuse ** 2 - side_a ** 2) ** (1 / 2)


def calculate_type(base, side_a, side_c, height):
    if side_a <= 0 or side_c <= 0:
        raise ValueError('Los lados deben ser mayores de 0')
    if side_a < height or side_c < height:
        raise ValueError('¿Es el mismo triángulo? Los lados no pueden ser menores que la altura')

    area = calculate_triangle_area(base, height)
    heron_area = _calculate_herons_area(side_a, base, side_c)

    if not isclose(area, heron_area, atol=0.01):
        raise ValueError('¿Es el mismo triángulo? Su área no concuerda con la del anterior')

    if side_a == height or side_c == height:
        type_by_angles = 'rectangulo'
    elif side_a < base and side_c < base:
        type_by_angles = 'actutangulo'
    else:
        type_by_angles = 'obtusangulo'

    if side_a == base == side_c:
        type_by_sides = 'equilátero'
    elif side_a == base or side_a == side_c or base == side_c:
        type_by_sides = 'isósceles'
    else:
        type_by_sides = 'escaleno'

    return f'{type_by_angles} {type_by_sides}'


def calculate_type_with_2_sides(side_a, side_b, height):
    if side_a <= 0 or side_b <= 0:
        raise ValueError('Los lados deben ser mayores de 0')
    if side_b <= height:
        raise ValueError('Los lados no pueden ser menores o iguales que la altura')

    side_c = 0
    hypotenuse = _get_hypotenuse(side_a, height)
    print('hipotenusa', hypotenuse)

    type_by_sides = ''
    type_by_angles = ''

    if isclose(hypotenuse, side_b):
        side_c = height
        type_by_angles = 'rectángulo'

    if isclose(side_a, side_b) and isclose(side_a, side_c):
        type_by_sides = 'equilátero'
    elif isclose(side_a, side_b) or isclose(side_a, side_c) or isclose(side_b, side_c):
        type_by_sides = 'isósceles'
    else:
        type_by_sides = 'escaleno'

    type = f'trinagulo {type_by_angles} {type_by_sides}'

    return type
