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
  q.questions,
  CAST(a.answers AS INTEGER) AS answers,
  a.created_time,
  a.modified_time
FROM answers a
JOIN users u      ON u.id = a.user_id
JOIN questions q  ON q.id = a.questions_id
JOIN drivers d    ON d.id = q.drivers_id
WHERE u.username = 'john_doe'
  AND d.drivers_name = 'Business Performance'
QUALIFY ROW_NUMBER() OVER (
  PARTITION BY q.id
  ORDER BY a.modified_time DESC, a.id DESC  -- tie-breaker on id
) = 1;