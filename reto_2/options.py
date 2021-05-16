from enum import Enum


def parse_option(value):
    for option in OPTIONS:
        if value == option.value[0]:
            return option
    raise ValueError('Valor no esta dentro de las opciones.')


class OPTIONS(Enum):
    PIEDRA = 1, ('TIJERA',)
    PAPEL = 2, ('PIEDRA',)
    TIJERA = 3, ('PAPEL',)

    def wins_against_options(self, option):
        wins_against = self.value[1]
        if option.name in wins_against:
            return True
        else:
            return False

    def get_option(self):
        return self.value[0]

