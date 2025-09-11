CREATE OR REPLACE SEQUENCE surveys_id_seq START 1; 
CREATE OR REPLACE TABLE surveys (
    id INTEGER PRIMARY KEY DEFAULT NEXTVAL('surveys_id_seq'),
    name VARCHAR,
    created_time  TIMESTAMP NOT NULL DEFAULT current_localtimestamp(),
    modified_time TIMESTAMP NOT NULL DEFAULT current_localtimestamp(),
);

INSERT INTO surveys (name) VALUES ('Testing Survey');
INSERT INTO surveys (name) VALUES ('Employee Satisfaction Survey');

select * from surveys;