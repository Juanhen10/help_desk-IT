# functions_/comandos.py

from models.database import session
from models.user import User
import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def add_user(username, password):
    hashed_password = hash_password(password)
    new_user = User(username=username, password=hashed_password)
    session.add(new_user)
    session.commit()

def authenticate(username, password):
    user = session.query(User).filter_by(username=username).first()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return True
    return False
