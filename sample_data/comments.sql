DROP TABLE IF EXISTS comments;
CREATE TABLE comments (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	submission_time VARCHAR(20) NOT NULL,
	question_id BIGINT REFERENCES questions(id),
	answer_id BIGINT REFERENCES answers(id),
	message VARCHAR(1000) NOT NULL
);
INSERT INTO comments (id, submission_time, question_id, answer_id, message) VALUES (1, '1576167982', 1, NULL, 'Not clear ... aaaa!!!!');
