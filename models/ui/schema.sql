DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    hashed_pin TEXT NOT NULL,
    departamento TEXT NOT NULL,
    is_admin BOOLEAN NOT NULL
);
