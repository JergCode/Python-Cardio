from enum import Enum


def parse_option(value):
    """The purpose of this function is to return an OPTION object when received an integer.
    If the number received is not within the Enum it raises an ValueError.
    @:param value Type: Integer
    @:returns OPTION Object
    """
    for option in OPTIONS:
        if value == option.value[0]:
            return option
    raise ValueError('Valor no esta dentro de las opciones.')


class OPTIONS(Enum):
    """The purpose of this Enum is to create default options and don't let users to give just any
    Option. The first parameter is the name (PIEDRA, PAPEL, TIJERA, etc...), the second is the option
    that the user will have to type, this will show in the menu something like:
        1 .- PIEDRA
        2 .- PAPEL
        3 .- TIJERA

    The thrid parameter is the OPTIONS that it can beat, so PIEDRA beats TIJERA, PAPEL beats PIEDRA, and so
    on.
        """
    PIEDRA = 1, ('TIJERA',)
    PAPEL = 2, ('PIEDRA',)
    TIJERA = 3, ('PAPEL',)

    def wins_against_options(self, option):
        """The purpose of this function is to return an OPTION object when received an integer.
            If the number received is not within the Enum it raises an ValueError.
            @:param value Type: Integer
            @:returns True if the self OPTION Object
            """
        wins_against = self.value[1]
        if option.name in wins_against:
            return True
        else:
            return False

    def get_option(self):
        return self.value[0]
