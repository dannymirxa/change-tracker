COPY drivers FROM 'schema/drivers.csv' (FORMAT 'csv', force_not_null 'id', quote '"', delimiter ',', header 1);
COPY surveys FROM 'schema/surveys.csv' (FORMAT 'csv', force_not_null ('created_time', 'modified_time', 'id'), quote '"', delimiter ',', header 1);
COPY users FROM 'schema/users.csv' (FORMAT 'csv', force_not_null ('username', 'id'), quote '"', delimiter ',', header 1);
COPY questions FROM 'schema/questions.csv' (FORMAT 'csv', force_not_null ('drivers_id', 'id'), quote '"', delimiter ',', header 1);
COPY answers FROM 'schema/answers.csv' (FORMAT 'csv', force_not_null ('user_id', 'questions_id', 'created_time', 'modified_time', 'id'), quote '"', delimiter ',', header 1);
