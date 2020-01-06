DROP TABLE IF EXISTS question_tags;
CREATE TABLE question_tags (
	question_id BIGINT REFERENCES questions(id),
	tag_id BIGINT REFERENCES tags(id)
);
