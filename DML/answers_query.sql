SELECT q.questions, cast(a.answers as INTEGER) answers, a.created_time, a.modified_time  FROM answers a
                        INNER JOIN users u on u.id = a.user_id
                        INNER JOIN questions q on q.id = a.questions_id
                        INNER JOIN drivers d on d.id = q.drivers_id
                        WHERE 1=1
                        AND u.username = 'john_doe'
                        AND d.drivers_name = 'Business Performance'
                        ;

SELECT
  q.id AS question_id,
  q.questions,
  arg_max(CAST(a.answers AS INTEGER), a.modified_time) AS answers,
  arg_max(a.created_time, a.modified_time)            AS created_time,
  MAX(a.modified_time)                                AS modified_time
FROM answers a
JOIN users u      ON u.id = a.user_id
JOIN questions q  ON q.id = a.questions_id
JOIN drivers d    ON d.id = q.drivers_id
WHERE u.username = 'john_doe'
  AND d.drivers_name = 'Business Performance'
GROUP BY q.id, q.questions;

SELECT
  q.questions, d.drivers_name,
  CAST(a.answers AS INTEGER) AS answers,
  a.created_time,
  a.modified_time
FROM answers a
JOIN users u      ON u.id = a.user_id
JOIN questions q  ON q.id = a.questions_id
JOIN drivers d    ON d.id = q.drivers_id
WHERE u.username = 'john_doe'
QUALIFY ROW_NUMBER() OVER (
  PARTITION BY q.id
  ORDER BY a.modified_time DESC, a.id DESC  -- tie-breaker on id
) = 1;

SELECT
                                drivers_name
                            FROM answers a
                                JOIN users u      ON u.id = a.user_id
                                JOIN questions q  ON q.id = a.questions_id
                                JOIN drivers d    ON d.id = q.drivers_id
                            WHERE u.username = 'john_doe'
                                QUALIFY ROW_NUMBER() OVER (
                                PARTITION BY q.id
                            ORDER BY a.modified_time DESC, a.id DESC
                            ) = 1;

WITH latest_answers AS (
  SELECT
    q.questions,
    d.drivers_name,
    CAST(a.answers AS INTEGER) AS answers
  FROM answers a
  JOIN users u      ON u.id = a.user_id
  JOIN questions q  ON q.id = a.questions_id
  JOIN drivers d    ON d.id = q.drivers_id
  WHERE u.username = 'john_doe'
  QUALIFY ROW_NUMBER() OVER (
    PARTITION BY q.id
    ORDER BY a.modified_time DESC, a.id DESC
  ) = 1
)
SELECT DISTINCT drivers_name
FROM latest_answers;

  SELECT
    q.id AS question_id,
    d.drivers_name,
    CAST(a.answers AS INTEGER) AS answers,
    a.modified_time
  FROM answers a
  JOIN users u      ON u.id = a.user_id
  JOIN questions q  ON q.id = a.questions_id
  JOIN drivers d    ON d.id = q.drivers_id
  WHERE u.username = 'john_doe'
  QUALIFY ROW_NUMBER() OVER (
    PARTITION BY q.id
    ORDER BY a.modified_time DESC, a.id DESC
  ) = 1

WITH latest_answers AS (
  SELECT
    q.id AS question_id,
    d.drivers_name,
    CAST(a.answers AS INTEGER) AS answers
  FROM answers a
  JOIN users u      ON u.id = a.user_id
  JOIN questions q  ON q.id = a.questions_id
  JOIN drivers d    ON d.id = q.drivers_id
  WHERE u.username = 'john_doe'
  QUALIFY ROW_NUMBER() OVER (
    PARTITION BY q.id
    ORDER BY a.modified_time DESC, a.id DESC
  ) = 1
)
SELECT
  drivers_name,
  -- COUNT(question_id) AS num_questions,
  -- SUM(answers) AS total_answers,
  ROUND(SUM(answers) * 1.0 / COUNT(question_id), 2) AS average_answer
FROM latest_answers
GROUP BY drivers_name;

WITH latest_answers AS (
  SELECT
      q.id AS question_id,
      d.drivers_name,
      CAST(a.answers AS INTEGER) AS answers
  FROM answers a
  JOIN users u      ON u.id = a.user_id
  JOIN questions q  ON q.id = a.questions_id
  JOIN drivers d    ON d.id = q.drivers_id
  WHERE u.username = 'john_doe'
  QUALIFY ROW_NUMBER() OVER (
      PARTITION BY q.id
      ORDER BY a.modified_time DESC, a.id DESC
  ) = 1
  )
  SELECT
  drivers_name,
  -- COUNT(question_id) AS num_questions,
  -- SUM(answers) AS total_answers,
  ROUND(SUM(answers) * 1.0 / COUNT(question_id), 2) AS average_answer
  FROM latest_answers
  GROUP BY drivers_name;

SELECT
    -- q.id AS question_id,
    d.drivers_name,
    CAST(a.answers AS INTEGER) AS answers
    -- a.modified_time
  FROM answers a
  JOIN users u      ON u.id = a.user_id
  JOIN questions q  ON q.id = a.questions_id
  JOIN drivers d    ON d.id = q.drivers_id
WHERE u.username = 'john_doe'
-- AND d.drivers_name = 'Business Performance'
QUALIFY ROW_NUMBER() OVER (
  PARTITION BY q.id
  ORDER BY a.modified_time DESC, a.id DESC
) = 1

SELECT
    -- q.id AS question_id,
    d.drivers_name,
    q.questions,
    CAST(a.answers AS INTEGER) AS answers
    -- a.modified_time
  FROM answers a
  JOIN users u      ON u.id = a.user_id
  JOIN questions q  ON q.id = a.questions_id
  JOIN drivers d    ON d.id = q.drivers_id
WHERE u.username = 'john_doe'
-- AND d.drivers_name = 'Benefits Realization'
QUALIFY ROW_NUMBER() OVER (
  PARTITION BY q.id
  ORDER BY a.modified_time DESC, a.id DESC
) = 1

WITH latest_answers AS (
                            SELECT
                                q.id AS question_id,
                                d.drivers_name,
                                CAST(a.answers AS INTEGER) AS answers
                            FROM answers a
                            JOIN users u      ON u.id = a.user_id
                            JOIN questions q  ON q.id = a.questions_id
                            JOIN drivers d    ON d.id = q.drivers_id
                            WHERE u.username = 'john_doe'
                            QUALIFY ROW_NUMBER() OVER (
                                PARTITION BY q.id
                                ORDER BY a.modified_time DESC, a.id DESC
                            ) = 1
                            )
                            SELECT
                            drivers_name,
                            -- COUNT(question_id) AS num_questions,
                            -- SUM(answers) AS total_answers,
                            ROUND(SUM(answers) * 1.0 / COUNT(question_id), 2) AS average_answer
                            FROM latest_answers
                            GROUP BY drivers_name;