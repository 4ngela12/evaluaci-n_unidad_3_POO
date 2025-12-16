import requests
from auxiliares.constante import API_BASE_URL

def obtener_todos():
    r = requests.get(f"{API_BASE_URL}/todos")
    r.raise_for_status()
    return r.json()

def crear_todo_api(title, completed, user_id):
    data = {
        "title": title,
        "completed": completed,
        "userId": int(user_id)
    }
    r = requests.post(f"{API_BASE_URL}/todos", json=data)
    r.raise_for_status()
    return r.json()

def actualizar_todo_api(todo_id, title, completed):
    if not str(todo_id).isdigit():
        raise Exception("El ID debe ser numérico")

    data = {
        "title": title,
        "completed": completed
    }
    r = requests.put(f"{API_BASE_URL}/todos/{todo_id}", json=data)
    r.raise_for_status()
    return r.json()

def eliminar_todo_api(todo_id):
    if not str(todo_id).isdigit():
        raise Exception("El ID debe ser numérico")

    r = requests.delete(f"{API_BASE_URL}/todos/{todo_id}")
    r.raise_for_status()
    return {"mensaje": "TODO eliminado correctamente"}
