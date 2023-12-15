from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Persona(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nombre     = db.Column(db.String(100), nullable=False) 
    usuario    = db.Column(db.String(100), unique=True, nullable=False)
    email      = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(100), nullable=False)
    
    def set_password(self, password):
        self.contrasena = generate_password_hash(password, method='pbkdf2:sha512')

    def check_password(self, password):
        return check_password_hash(self.contrasena, password)
