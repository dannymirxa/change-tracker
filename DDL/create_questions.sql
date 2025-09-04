-- Active: 1756648795144@@127.0.0.1@3306


CREATE OR REPLACE SEQUENCE questions_id_seq START 1; 
CREATE OR REPLACE TABLE questions (
    id INTEGER PRIMARY KEY DEFAULT NEXTVAL('questions_id_seq'),
    questions varchar,
    drivers_id INTEGER not null,
    FOREIGN KEY (drivers_id) REFERENCES drivers(id)
);

-- INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'Your Department''s (i.e. Operations, Merchandising etc.) effectiveness', 1);
-- INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'The level of customer service (internal or external) your Team provides', 1);
-- INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'Managing costs and resources in your Team', 1);
-- INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'Increases in revenue', 2);
-- INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'Reduced costs', 2);
-- INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'Improved customer shopping experience', 2);
-- INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'Better efficiency and productivity', 2);
-- INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'Greater team collaboration and communication', 2);
-- INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'Better resource management', 2);
-- INSERT INTO questions VALUES (NEXTVAL('questions_id_seq'), 'How confident are you that the performance of your Department will improve because 7-Eleven''s transformation has been implemented?', 2);


insert into 
  questions (id, questions, drivers_id, qcode) values 
  (NEXTVAL('questions_id_seq'), 'Your team''s effectiveness at getting work done', 1, 'bpb|effectiveness');
insert into 
  questions (id, questions, drivers_id, qcode) values 
 (NEXTVAL('questions_id_seq'), 'The level of service your team provides to internal/external customers (e.g. HR serves employees (internal customers), Finance serves vendors (external customers), Researchers support scientific findings)', 1, 'bpb|customer_service');
insert into 
  questions (id, questions, drivers_id, qcode) values 
  (NEXTVAL('questions_id_seq'), 'Managing costs and resources in your organisation / team', 1, 'bpb|change_cost_management');
insert into 
  questions (id, questions, drivers_id, qcode) values 
  (NEXTVAL('questions_id_seq'), 'Team alignment between A*STAR and Research Entities on HR, FIN, Procurement and Scholarship processes', 2, 'sfa|increased_alignment_business');
insert into 
  questions (id, questions, drivers_id, qcode) values 
  (NEXTVAL('questions_id_seq'), 'Time savings through simplified HR, Finance, procurement, scholarship and employee-related functionalities and processes', 2, 'sfa|auto_benefits_better_integration');
insert into 
  questions (id, questions, drivers_id, qcode) values 
  (NEXTVAL('questions_id_seq'), 'Improved employee experience through a digital front door', 2, 'sfa|benefits_employee_exp');
insert into 
  questions (id, questions, drivers_id, qcode) values 
  (NEXTVAL('questions_id_seq'), 'A scalable workforce with enhanced insights (e.g., spend, talent, supplier visibility) and data-driven decision-making capabilities', 2, 'sfa|auto_benefits_better_data-driven_decisions');
insert into 
  questions (id, questions, drivers_id, qcode) values 
  (NEXTVAL('questions_id_seq'), 'How confident are you that the performance of your team will improve because ERP 2.0 has been implemented?', 2, 'sfb|lv1_success');

SELECT * FROM questions;