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

INSERT INTO users (id, name, hashed_password, is_active, is_admin)
VALUES  (1, 'Ben', convert_to('password', 'UTF-8'), TRUE, TRUE),
        (2, 'Megan', convert_to('secretpass', 'UTF-8'), TRUE, TRUE),
        (3, 'Chip', convert_to('treatsplz', 'UTF-8'), TRUE, TRUE),
        (4, 'Libby', convert_to('iluvsqueakyball', 'UTF-8'), TRUE, TRUE),
        (5, 'Lou Lou', convert_to('feedmehumans', 'UTF-8'), TRUE, TRUE);

CREATE TABLE collections (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    description TEXT,
    created_ts TIMESTAMPTZ DEFAULT NOW(),
    is_private BOOLEAN DEFAULT FALSE,
    user_id INT REFERENCES users(id)
);

INSERT INTO collections (id, name, description, user_id)
VALUES  (1, 'Reading', 'Books I''m currently reading', 1),
        (2, 'Want To Read', 'Collection of books I plan to read', 1),
        (3, 'Read', 'Books I''ve already finished', 1),
        (4, 'Megan''s Collection', 'This is Megan''s collection', 2),
        (5, 'Chip''s Collection', 'This is Chip''s collection', 3),
        (6, 'Libby''s Collection', 'This is Libby''s collection', 4),
        (7, 'Lou Lou''s Collection', 'This is Lou Lou''s collection', 5);

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

INSERT INTO books (id, title, author, description, collection_id)
VALUES  (1, 'The Great Gatsby', 'F. Scott Fitzgerald', 'A classic novel about the American Dream', 1),
        (2, 'The Catcher in the Rye', 'J.D. Salinger', 'A novel about teenage angst', 1),
        (3, 'The Bell Jar', 'Sylvia Plath', 'A novel about a young', 2),
        (4, 'The Road', 'Cormac McCarthy', 'A novel about a father and son', 2),
        (5, 'The Hobbit', 'J.R.R. Tolkien', 'A novel about a hobbit', 3),
        (6, 'The Lord of the Rings', 'J.R.R. Tolkien', 'A novel about a ring', 3),
        (7, 'The Hunger Games', 'Suzanne Collins', 'A novel about a dystopian future', 4),
        (8, 'Catching Fire', 'Suzanne Collins', 'A novel about a dystopian future', 4),
        (9, 'Mockingjay', 'Suzanne Collins', 'A novel about a dystopian future', 4),
        (10, 'The Giver', 'Lois Lowry', 'A novel about a dystopian future', 5),
        (11, 'Gathering Blue', 'Lois Lowry', 'A novel about a dystopian future', 5),
        (12, 'Messenger', 'Lois Lowry', 'A novel about a dystopian future', 5);