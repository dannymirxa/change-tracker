CREATE OR REPLACE SEQUENCE users_id_seq START 1; 

CREATE OR REPLACE TABLE users (
    id INTEGER PRIMARY KEY DEFAULT NEXTVAL('users_id_seq'),
    username VARCHAR NOT NULL,
    email VARCHAR
);

INSERT INTO users VALUES (NEXTVAL('users_id_seq'), 'john_doe', 'john.doe@example.com');
INSERT INTO users VALUES (NEXTVAL('users_id_seq'), 'jane_smith', 'jane.smith@example.com');

SELECT * FROM users;