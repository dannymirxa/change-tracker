CREATE OR REPLACE SEQUENCE users_id_seq START 1; 

CREATE OR REPLACE TABLE users (
    id INTEGER PRIMARY KEY DEFAULT NEXTVAL('users_id_seq'),
    username VARCHAR NOT NULL,
    email VARCHAR
);

INSERT INTO users VALUES (NEXTVAL('users_id_seq'), 'john_doe', 'john.doe@example.com');
INSERT INTO users VALUES (NEXTVAL('users_id_seq'), 'jane_smith', 'jane.smith@example.com');
INSERT INTO users VALUES (NEXTVAL('users_id_seq'), 'stephanie_song', 'shuet.yee.song@accenture.com');
INSERT INTO users VALUES (NEXTVAL('users_id_seq'), 'emily_wong', 'emily.a.wong@accenture.com');
INSERT INTO users VALUES (NEXTVAL('users_id_seq'), 'yap_shyne', 'shyne.yap@accenture.com');
INSERT INTO users VALUES (NEXTVAL('users_id_seq'), 'aisha_yusuf', 'aisha.yusuf@accenture.com');
INSERT INTO users VALUES (NEXTVAL('users_id_seq'), 'danial_mirza', 'danial.m.bin.madrawi@accenture.com');


SELECT * FROM users;