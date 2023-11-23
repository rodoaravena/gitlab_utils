import api
import sys
import os

def check_os():
    if sys.platform == "linux" or sys.platform == "linux2":
        return lambda : os.system('clear')
    elif sys.platform == "darwin":
        return lambda : os.system('clear')
    elif sys.platform == "win32":
        return lambda : os.system('cls')

clear = check_os()

def menu():
    print("¿Qué desea hacer?")
    print("1.- Registrar usuario")
    print("2.- Registrar usuarios desde un archivo")
    print("3.- Salir")
    
    op = input("Opción: ")
    if op == '1':
        clear()
        print("No implementado")
        
    elif op == '2':
        clear()
        api.register_bulk_users()
    elif op == '3':
        return
    else:
        clear()
        print("Opción invalida")
    menu()
    

def main():
    clear()
    menu()
    return 0


if __name__== "__main__":
    sys.exit(main())