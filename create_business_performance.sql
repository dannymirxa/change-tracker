

CREATE OR REPLACE SEQUENCE questions_id_seq START 1; 
CREATE OR REPLACE TABLE questions (
    id INTEGER PRIMARY KEY DEFAULT NEXTVAL('questions_id_seq'),
    questions varchar,
    drivers_id INTEGER not null,
    FOREIGN KEY (drivers_id) REFERENCES drivers(id)
);

INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'Your Department''s (i.e. Operations, Merchandising etc.) effectiveness', 1);
INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'The level of customer service (internal or external) your Team provides', 1);
INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'Managing costs and resources in your Team', 1);

SELECT * FROM questions;
TRUNCATE TABLE questions;

CREATE OR REPLACE SEQUENCE answers_id_seq START 1; 
CREATE OR REPLACE TABLE answers (
    id INTEGER PRIMARY KEY DEFAULT NEXTVAL('answers_id_seq'),
    user_id INTEGER not null,
    questions_id INTEGER not null,
    answers varchar,
    FOREIGN KEY (questions_id) REFERENCES questions(id)
);