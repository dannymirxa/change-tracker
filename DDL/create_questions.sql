-- Active: 1756648795144@@127.0.0.1@3306


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
INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'Increases in revenue', 2);
INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'Reduced costs', 2);
INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'Improved customer shopping experience', 2);
INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'Better efficiency and productivity', 2);
INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'Greater team collaboration and communication', 2);
INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'Better resource management', 2);
INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'How confident are you that the performance of your Department will improve because 7-Eleven''s transformation has been implemented?', 2);

SELECT id, questions FROM questions;