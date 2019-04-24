

texto_subrayar = input("Escribe una frase:")


def subtext(valor):
    numero_guiones = ""
    for i in valor:
        numero_guiones += "_"
    return numero_guiones

print(texto_subrayar)
print(subtext(texto_subrayar))

