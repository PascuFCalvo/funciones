import pickle

from time import sleep


ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5
SAVE_FILE_NAME = "contacts.save"
MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]


def ask_until_option_expected(options):

    selected_action = ""
    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in (options)):
        selected_action = input("elige una opcion ")

    return int(selected_action)



def show_menu():


    print("Acciones disponinbles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar un contacto")
    print("4 - Exportar contactos a un CSV")
    print("5 - Salir")
    return ask_until_option_expected(MENU_OPTIONS)


def add_contact(contacts):


    print("\nAñadir contacto\n")
    contact = {
        "name": input("Nombre: "),
        "phone": input("Teléfono: "),
        "email": input("Email: ")
    }
    contacts.append(contact)
    print("Se ha añadido el contacto {} correctamente\n".format(contact["name"]))
    sleep(2)


def remove_contact(contacts):
    print("\nBuscar contacto para borrar\n")
    search_term = input("Introducir el nombre del contacto o parte de él: ")
    found_contacts = []

    print("He encontrado los siguientes contactos:")
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se ha encontrado ninguno.")

    contacts.pop(contact_index)
    print("Contacto eliminado.")
    sleep(2)


def find_contact(contacts):
    search_variable = ""
    ask_variable = ""

    print("\n\nBuscar contacto\n")
    option_search = input("¿Quieres buscar el contacto por:\n1- nombre\n2 -email\n\n")
    if option_search == "1":
            search_variable = "name"
            ask_variable = "nombre"
    elif option_search == "2":
            search_variable = "email"
            ask_variable = "email"

    search_term = input("Introducir el {} del contacto o parte de él:. ".format(ask_variable))
    found_contacts = []

    print("He encontrado los siguientes contactos:")
    sleep(1)
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if contact[search_variable].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact[search_variable]))
            contact_indexes.append(contact_counter)
            contact_counter += 1


    try_again = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)

        print("\nInformación sobre {}\n".format(found_contacts[contact_index][search_variable]))
        print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**found_contacts[contact_index]))
        sleep(2)

    elif len(contact_indexes) == 0:
        try_again = input("No se ha encontrado ninguno, volver a buscar?\n1- SI\n2- NO")

    if try_again == "1":
        find_contact(contacts)

    if try_again == "2":
        show_menu()


def export_contacts():
    pass


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente.")


def main():
    contacts = load_contacts()
    action = show_menu()

    while action != ACTION_EXIT:
        if action == ACTION_ADD_CONTACT:
            add_contact(contacts)
        elif action == ACTION_REMOVE_CONTACT:
            remove_contact(contacts)
        elif action == ACTION_FIND_CONTACT:
            find_contact(contacts)
        elif action == ACTION_EXPORT_CONTACT:
            export_contacts()

        action = show_menu()

    save_contacts(contacts)
    print("¡Adiós!")


if __name__ == "__main__":
    main()
