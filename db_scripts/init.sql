CREATE DATABASE test_db;

\c test_db;

-- CREATE SCHEMA booked;

-- Creates users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    hashed_password BYTEA NOT NULL,
    created_ts TIMESTAMPTZ DEFAULT NOW(),
    is_active BOOLEAN DEFAULT FALSE,
    is_admin BOOLEAN DEFAULT FALSE
);

INSERT INTO users (name, hashed_password, is_active, is_admin)
VALUES  ('Ben', convert_to('password', 'UTF-8'), TRUE, TRUE),
        ('Megan', convert_to('secretpass', 'UTF-8'), TRUE, TRUE),
        ('Chip', convert_to('treatsplz', 'UTF-8'), TRUE, TRUE),
        ('Libby', convert_to('iluvsqueakyball', 'UTF-8'), TRUE, TRUE),
        ('Lou Lou', convert_to('feedmehumans', 'UTF-8'), TRUE, TRUE);

CREATE TABLE collections (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    description TEXT,
    created_ts TIMESTAMPTZ DEFAULT NOW(),
    is_private BOOLEAN DEFAULT FALSE,
    user_id INT REFERENCES users(id)
);

INSERT INTO collections (name, description, user_id)
VALUES  ('Reading', 'Books I''m currently reading', 1),
        ('Want To Read', 'Collection of books I plan to read', 1),
        ('Read', 'Books I''ve already finished', 1),
        ('Megan''s Collection', 'This is Megan''s collection', 2),
        ('Chip''s Collection', 'This is Chip''s collection', 3),
        ('Libby''s Collection', 'This is Libby''s collection', 4),
        ('Lou Lou''s Collection', 'This is Lou Lou''s collection', 5);

UPDATE collections
SET is_private = TRUE
WHERE id = 1 OR id = 2;

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    description TEXT,
    collected_ts TIMESTAMPTZ DEFAULT NOW(),
    collection_id INT REFERENCES collections(id)
);

INSERT INTO books (title, author, description, collection_id)
VALUES  ('The Great Gatsby', 'F. Scott Fitzgerald', 'A classic novel about the American Dream', 1),
        ('The Catcher in the Rye', 'J.D. Salinger', 'A novel about teenage angst', 1),
        ('The Bell Jar', 'Sylvia Plath', 'A novel about a young', 2),
        ('The Road', 'Cormac McCarthy', 'A novel about a father and son', 2),
        ('The Hobbit', 'J.R.R. Tolkien', 'A novel about a hobbit', 3),
        ('The Lord of the Rings', 'J.R.R. Tolkien', 'A novel about a ring', 3),
        ('The Hunger Games', 'Suzanne Collins', 'A novel about a dystopian future', 4),
        ('Catching Fire', 'Suzanne Collins', 'A novel about a dystopian future', 4),
        ('Mockingjay', 'Suzanne Collins', 'A novel about a dystopian future', 4),
        ('The Giver', 'Lois Lowry', 'A novel about a dystopian future', 5),
        ('Gathering Blue', 'Lois Lowry', 'A novel about a dystopian future', 5),
        ('Messenger', 'Lois Lowry', 'A novel about a dystopian future', 5);