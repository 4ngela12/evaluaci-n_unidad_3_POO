import pwinput
from negocio.procesar import (
    registrar_usuario,
    login,
    importar_todos_desde_api,
    crear_todo_negocio,
    actualizar_todo_negocio,
    eliminar_todo_negocio,
)
from datos.db import init_db
from auxiliares.helpers import titulo

def menu():
    print("\n1) Registrar usuario")
    print("2) Login")
    print("3) Importar TODOS desde API")
    print("4) Crear TODO (POST)")
    print("5) Actualizar TODO (PUT)")
    print("6) Eliminar TODO (DELETE)")
    print("0) Salir")
    return input("Opción: ")

def main():
    init_db()
    titulo("          Sistema iniciado           ")

    while True:
        opcion = menu()

        try:
            if opcion == "1":
                registrar_usuario(
                    input("Nombre: "),
                    input("Username: "),
                    input("Email: "),
                    pwinput.pwinput("Contraseña: ")
                )
                print("Usuario registrado")

            elif opcion == "2":
                login(input("Username: "), pwinput.pwinput("Contraseña: "))
                print("Login correcto")

            elif opcion == "3":
                print(f"Importados {importar_todos_desde_api()} TODOS")

            elif opcion == "4":
                print(crear_todo_negocio(
                    input("Título: "),
                    input("¿Completado? (si/no): ").lower() == "si",
                    input("UserId: ")
                ))

            elif opcion == "5":
                print(actualizar_todo_negocio(
                    input("ID: "),
                    input("Nuevo título: "),
                    input("¿Completado? (si/no): ").lower() == "si"
                ))

            elif opcion == "6":
                print(eliminar_todo_negocio(input("ID: ")))

            elif opcion == "0":
                input("opcion valida ....!Adios¡")
                break

            else:
                print("Opción inválida")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
