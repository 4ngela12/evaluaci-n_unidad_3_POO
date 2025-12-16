from datos.db import SessionLocal
from modelos.usuario import Usuario
from modelos.todo import Todo

def create_user(nombre, username, email, password):
    db = SessionLocal()
    user = Usuario(
        nombre=nombre,
        username=username,
        email=email,
        password=password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user

def get_user_by_username(username):
    db = SessionLocal()
    user = db.query(Usuario).filter(Usuario.username == username).first()
    db.close()
    return user

def guardar_todos(lista_todos):
    db = SessionLocal()
    for t in lista_todos:
        todo = Todo(
            id=t["id"],
            title=t["title"],
            completed=t["completed"],
            user_id=t["userId"]
        )
        db.merge(todo)
    db.commit()
    db.close()



