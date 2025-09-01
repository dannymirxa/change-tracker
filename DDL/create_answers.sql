CREATE OR REPLACE SEQUENCE answers_id_seq START 1; 
CREATE OR REPLACE TABLE answers (
    id INTEGER PRIMARY KEY DEFAULT NEXTVAL('answers_id_seq'),
    user_id INTEGER not null,
    questions_id INTEGER not null,
    answers varchar,
    created_time  TIMESTAMP NOT NULL DEFAULT current_localtimestamp(),
    modified_time TIMESTAMP NOT NULL DEFAULT current_localtimestamp(),
    FOREIGN KEY (questions_id) REFERENCES questions(id)
);

select * from answers;