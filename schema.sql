CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT UNIQUE NOT NULL, password TEXT NOT NULL, type INTEGER);

CREATE TABLE categories (id SERIAL PRIMARY KEY, name TEXT UNIQUE NOT NULL, description TEXT, type INTEGER);
INSERT INTO categories (name, description, type) VALUES ('Turhat turinat', 'kaikkien kirjautuneiden käyttäjien oma turinointitupa', 3);
INSERT INTO categories (name, description, type) VALUES ('Löysät löpinät', 'kaikille kirjautuneille vapaa alue jossa sopii löpistä löysempiä hengentuotteita', 3);
INSERT INTO categories (name, description, type) VALUES ('Salaiset supinat', 'enabloitu erikoisoikeuden saaneiden erikoishenkilöiden erityisen salaisille aiheille', 2);
INSERT INTO categories (name, description, type) VALUES ('Ylläpitäjäin yskökset', 'ainoastaan adminien ajatustenvirralle', 1);

CREATE TABLE threads (id SERIAL PRIMARY KEY, name TEXT UNIQUE NOT NULL, category_id INTEGER REFERENCES categories);

CREATE TABLE messages (id SERIAL PRIMARY KEY, content TEXT, category_id INTEGER REFERENCES categories, thread_id INTEGER REFERENCES threads, user_id INTEGER REFERENCES users, time TIMESTAMP, visibility BOOLEAN);


