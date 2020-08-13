CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT UNIQUE, password TEXT, type INTEGER);
CREATE TABLE categories (id SERIAL PRIMARY KEY, name TEXT UNIQUE, description TEXT, type INTEGER);
INSERT INTO categories (name, description, type) VALUES ('Turhat turinat', 'kaikkien kirjautuneiden käyttäjien oma turinointitupa', 3);
INSERT INTO categories (name, description, type) VALUES ('Löysät löpinät', 'kaikille kirjautuneille vapaa alue jossa sopii löpistä löysempiä tuotteita', 3);
INSERT INTO categories (name, description, type) VALUES ('Salaiset supinat', 'enabloitu erikoisoikeuden saaneiden erikoishenkilöiden erityisen salaisille aiheille', 2);
INSERT INTO categories (name, description, type) VALUES ('Ylläpitäjäin yskökset', 'ainoastaan adminien ajatustenvirralle', 1);
