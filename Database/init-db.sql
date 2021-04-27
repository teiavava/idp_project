CREATE TABLE IF NOT EXISTS phones (
    id serial PRIMARY KEY,
    phone_model varchar NOT NULL,
    phone_os varchar NOT NULL,
    price varchar NOT NULL,
    stock INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    id serial PRIMARY KEY,
    username varchar NOT NULL UNIQUE,
	password varchar NOT NULL,
	role varchar NOT NULL,
    cash double PRECISION NOT NULL,
    email varchar UNIQUE,
);
