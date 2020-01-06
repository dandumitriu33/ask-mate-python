DROP TABLE IF EXISTS questions;
CREATE TABLE questions (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    submission_time VARCHAR (20) NOT NULL,
    view_number NUMERIC NOT NULL,
    vote_number NUMERIC NOT NULL,
    title VARCHAR(100) NOT NULL,
    message VARCHAR (1000),
    image VARCHAR (1000)
);
insert into questions (id, submission_time, view_number, vote_number, title, message, image) values (1, '1493368154', 94, 56, 'How to make lists in Python?', 'I am totally new to this, any hints?', null);
insert into questions (id, submission_time, view_number, vote_number, title, message, image) values (2, '1493068124', 82, 86, 'Wordpress loading multiple jQuery Versions', 'I developed a plugin that uses the jquery booklet plugin (http://builtbywill.com/booklet/#/) this plugin binds a function to $ so I cann call $(''.myBook'').booklet(); I could easy managing the loading order with wp_enqueue_script so first I load jquery then I load booklet so everything is fine. BUT in my theme i also using jquery via webpack so the loading order is now following: jquery booklet app.js (bundled file with webpack, including jquery)', '/static/img/codesample.png');
insert into questions (id, submission_time, view_number, vote_number, title, message, image) values (3, '1493015432', 32, 70, 'Drawing canvas with an image picked with Cordova Camera Plugin	', 'I''m getting an image from device and drawing a canvas with filters using Pixi JS. It works all well using computer to get an image. But when I''m on IOS, it throws errors such as cross origin issue, or that I''m trying to use an unknown format.', null );

