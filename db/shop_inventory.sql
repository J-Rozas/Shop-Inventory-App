DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS publishers;

CREATE TABLE publishers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(100),
    address VARCHAR(100)
);

CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    number_of_pages INT,
    genre VARCHAR(100),
    author VARCHAR(100),
    stock INT,
    selling_price FLOAT,
    publisher_id SERIAL REFERENCES publishers(id) ON DELETE CASCADE
);