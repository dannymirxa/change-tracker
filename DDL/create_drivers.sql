-- Active: 1756648795144@@127.0.0.1@3306
CREATE OR REPLACE SEQUENCE drivers_id_seq START 1; 

CREATE OR REPLACE TABLE drivers (
    id INTEGER PRIMARY KEY DEFAULT NEXTVAL('drivers_id_seq'),
    drivers_name varchar
);

INSERT INTO drivers VALUES (NEXTVAL('drivers_id_seq'), 'Business Performance');
INSERT INTO drivers VALUES (NEXTVAL('drivers_id_seq'), 'Benefits Realization');


SELECT * FROM drivers;