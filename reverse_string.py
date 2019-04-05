

def reverse_string(string_a_girar):
    nueva_string = ""
    indice_actual = len(string_a_girar) -1

    while indice_actual >= 0:
       nueva_string += string_a_girar[indice_actual]
       indice_actual -= 1
    return nueva_string


string_girada = reverse_string("Hola")
print(string_girada)