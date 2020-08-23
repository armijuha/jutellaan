CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT UNIQUE, password TEXT, type INTEGER);
INSERT INTO users (id, name, password, type) VALUES (1, 'Cicero', 'pisero', 3);

CREATE TABLE categories (id SERIAL PRIMARY KEY, name TEXT UNIQUE, description TEXT, type INTEGER);
INSERT INTO categories (name, description, type) VALUES ('Turhat turinat', 'kaikkien kirjautuneiden käyttäjien oma turinointitupa', 3);
INSERT INTO categories (name, description, type) VALUES ('Löysät löpinät', 'kaikille kirjautuneille vapaa alue jossa sopii löpistä löysempiä hengentuotteita', 3);
INSERT INTO categories (name, description, type) VALUES ('Salaiset supinat', 'enabloitu erikoisoikeuden saaneiden erikoishenkilöiden erityisen salaisille aiheille', 2);
INSERT INTO categories (name, description, type) VALUES ('Ylläpitäjäin yskökset', 'ainoastaan adminien ajatustenvirralle', 1);

CREATE TABLE threads (id SERIAL PRIMARY KEY, name TEXT UNIQUE, category_id INTEGER REFERENCES categories);
INSERT INTO threads (name, category_id) VALUES ('Testiturinaa toiminnan testaamiseksi', 1);
INSERT INTO threads (name, category_id) VALUES ('Taas turistaan ja töristään toistamiseen', 1);
INSERT INTO threads (name, category_id) VALUES ('Laitetaan luikaus löpinääkin lisäksi', 2);
INSERT INTO threads (name, category_id) VALUES ('Se on salaisuus, se on salaisuus...', 3);

CREATE TABLE messages (id SERIAL PRIMARY KEY, content TEXT, category_id INTEGER REFERENCES categories, thread_id INTEGER REFERENCES threads, user_id INTEGER REFERENCES users, time TIMESTAMP, visibility BOOLEAN);
INSERT INTO messages (content, category_id, thread_id, user_id, time, visibility) VALUES ('Testiähän se pukkaa tulemaan.Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat. Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 1, 1, 1, NOW(),True);

