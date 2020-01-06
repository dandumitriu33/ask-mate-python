DROP TABLE IF EXISTS answers;
CREATE TABLE answers (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	submission_time VARCHAR(20) NOT NULL,
	vote_number NUMERIC,
	question_id BIGINT NOT NULL REFERENCES questions(id),
	message VARCHAR(1000) NOT NULL,
	image VARCHAR(1000)
);
insert into answers (id, submission_time, vote_number, question_id, message, image) values (1, '1576167982', 58, 1, 'Good question. One time...', null);
insert into answers (id, submission_time, vote_number, question_id, message, image) values (2, '1576167983', 97, 1, 'AAh yes, I too remember the first time I ...', null);
insert into answers (id, submission_time, vote_number, question_id, message, image) values (3, '1576167984', 69, 2, 'I knew the answer but I forgot. Will get back to you if I remember.', null);
insert into answers (id, submission_time, vote_number, question_id, message, image) values (4, '1576167985', 20, 2, 'Was there a movie about this?', null);
insert into answers (id, submission_time, vote_number, question_id, message, image) values (5, '1576167986', 20, 3, 'Yikes.', null);
