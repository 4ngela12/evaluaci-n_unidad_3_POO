from datos.repo import create_user, get_user_by_username, guardar_todos
from negocio.auth import Encriptador
from servicios.api import (
    obtener_todos,
    crear_todo_api,
    actualizar_todo_api,
    eliminar_todo_api,
)

def registrar_usuario(nombre, username, email, password):
    enc = Encriptador()
    password_hash = enc.encriptar(password)
    return create_user(nombre, username, email, password_hash)

def login(username, password):
    user = get_user_by_username(username)
    if not user:
        raise Exception("Usuario no existe")

    enc = Encriptador()
    if not enc.verificar(password, user.password):
        raise Exception("Contraseña incorrecta")

    return user

def importar_todos_desde_api():
    todos = obtener_todos()
    guardar_todos(todos)
    return len(todos)

def crear_todo_negocio(title, completed, user_id):
    return crear_todo_api(title, completed, user_id)

def actualizar_todo_negocio(todo_id, title, completed):
    return actualizar_todo_api(todo_id, title, completed)

def eliminar_todo_negocio(todo_id):
    return eliminar_todo_api(todo_id)
