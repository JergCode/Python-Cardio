import math


def calculate_volume(option, requirements):
    volume = dict({
        'Esfera': lambda x: get_spheres_volume(x),
        'Cilindro': lambda x: get_cylinders_volume(x),
        'Cubo': lambda x: get_cubes_volume(x),
        'Prisma Triangular': lambda x: get_triangle_prism_volume(x),
        'Ortoedro': lambda x: get_cuboids_volume(x),
    })
    volume_formula = volume.get(option)
    return volume_formula(requirements)


def get_spheres_volume(requirements):
    radio, = requirements
    return (4 / 3) * math.pi * radio ** 3


def get_cylinders_volume(requirements):
    radio, height = requirements
    area = __circle_area(radio)
    return area * height


def get_cubes_volume(requirements):
    side, = requirements
    return side ** 3


def get_triangle_prism_volume(requirements):
    a, b, c, h = requirements
    area = __triangle_area(a, b, c)
    return area * h


def get_cuboids_volume(requirements):
    a, b, h = requirements
    return a * b * h


def __circle_area(radio):
    return math.pi * radio ** 2


def __triangle_area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
