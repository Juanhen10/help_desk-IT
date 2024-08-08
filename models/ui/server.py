import os
import sqlite3
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)

# Função para inicializar o banco de dados
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,     
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            departamento TEXT NOT NULL,
            pin TEXT NOT NULL,
            is_admin BOOLEAN NOT NULL,
            imagem BLOB
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    nome = data.get('nome')
    email = data.get('email')
    departamento = data.get('departamento')
    pin = data.get('pin')
    is_admin = data.get('is_admin')
    imagem_base64 = data.get('imagem')  # Recebe a imagem em base64

    try:
        # Converter a imagem de base64 para bytes
        imagem_bytes = base64.b64decode(imagem_base64)
    except Exception as e:
        return jsonify({'error': 'Erro ao decodificar a imagem base64'}), 400

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Verificar se o e-mail já existe
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    existing_user = cursor.fetchone()
    if existing_user:
        conn.close()
        return jsonify({'error': 'Email já existe'}), 409

    cursor.execute('''
        INSERT INTO users (nome, email, departamento, pin, is_admin, imagem)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nome, email, departamento, pin, is_admin, imagem_bytes))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Usuário registrado com sucesso!'})

@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, email, departamento, pin, is_admin FROM users')
    users = cursor.fetchall()
    conn.close()

    users_list = []
    for user in users:
        users_list.append({
            'id': user[0],
            'nome': user[1],
            'email': user[2],
            'departamento': user[3],
            'pin': user[4],
            'is_admin': user[5]
        })

    return jsonify(users_list)

if __name__ == '__main__':
    app.run(debug=True)
