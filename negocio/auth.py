import bcrypt

class Encriptador:
    def encriptar(self, texto):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(texto.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    def verificar(self, texto_plano, hash_guardado):
        return bcrypt.checkpw(texto_plano.encode('utf-8'), hash_guardado.encode('utf-8'))
