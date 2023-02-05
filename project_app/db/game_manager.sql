DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS publishers;

CREATE TABLE publishers (
    id SERIAL PRIMARY KEY,
    publisher_name VARCHAR(255),
    contact_details VARCHAR(255)
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    developer VARCHAR(255),
    genre VARCHAR(255),
    wholesale INT,
    price INT,
    stock INT,
    publisher_id INT NOT NULL REFERENCES publishers(id)
);