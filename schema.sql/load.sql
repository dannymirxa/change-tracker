COPY drivers FROM 'schema.sql/drivers.csv' (FORMAT 'csv', force_not_null 'id', quote '"', delimiter ',', header 1);
COPY users FROM 'schema.sql/users.csv' (FORMAT 'csv', force_not_null ('username', 'id'), quote '"', delimiter ',', header 1);
COPY questions FROM 'schema.sql/questions.csv' (FORMAT 'csv', force_not_null ('drivers_id', 'id'), quote '"', delimiter ',', header 1);
COPY answers FROM 'schema.sql/answers.csv' (FORMAT 'csv', force_not_null ('user_id', 'questions_id', 'created_time', 'modified_time', 'id'), quote '"', delimiter ',', header 1);
