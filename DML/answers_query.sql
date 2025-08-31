SELECT q.questions, cast(a.answers as INTEGER) answers, a.created_time, a.modified_time  FROM answers a
                        INNER JOIN users u on u.id = a.user_id
                        INNER JOIN questions q on q.id = a.questions_id
                        INNER JOIN drivers d on d.id = q.drivers_id
                        WHERE 1=1
                        AND u.username = 'john_doe'
                        AND d.drivers_name = 'Business Performance'
                        ;

