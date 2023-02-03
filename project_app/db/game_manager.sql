DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS publishers;

CREATE TABLE publishers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_details(255)
    );

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    developer VARCHAR(255),
    publisher_id INT NOT NULL REFERENCES publishers(id)
    genre VARCHAR(255),
    wholesale INT,
    price INT,
    stock INT
)