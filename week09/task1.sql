CREATE TABLE languages(
  id INTEGER PRIMARY KEY,
  language VARCHAR(25),
  answer TEXT,
  answered INTEGER,
  guide TEXT 
  );

INSERT INTO languages
VALUES(1, 'Python', 'google', 0, 'A folder named Python was created. Go there and fight with program.py!');
 
INSERT INTO languages
VALUES(2, 'Go',	'200 OK', 0, 'A folder named Go was created. Go there and try to make Google Go run.');

INSERT INTO languages
VALUES(3, 'Java', 'object oriented programming', 0, 'A folder named Java was created. Can you handle the class?');

INSERT into languages
VALUES(4, 'Haskell', 'Lambda', 0, 'Something pure has landed. Go to Haskell folder and see it!');

INSERT Into languages
VALUES(5, 'C#', 'NDI=', 0, 'Do you see sharp? Go to the C# folder and check out.');

INSERT INTO languages
VALUES(6, 'Ruby', 'https://www.ruby-lang.org/bg/', 0, 'Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!');

INSERT INTO languages
VALUES(7, 'C++', 'header files', 0, "Here be dragons! It's C++ time. Go to the C++ folder.");

INSERT INTO languages
VALUES(8, 'JavaScript', 'Douglas Crockford', 0, "NodeJS time. Go to JavaScript folder and Node your way!");

ALTER TABLE languages
ADD COLUMN rating INTEGER CHECK(rating BETWEEN 1 AND 9);

UPDATE languages
SET rating = 9
where id = 1;

UPDATE languages
SET rating = 5
where id = 2;

UPDATE languages
SET rating = 1
where id = 3;

UPDATE languages
SET rating = 8
where id = 4;

UPDATE languages
SET rating = 6
where id = 5;

UPDATE languages
SET rating = 7
where id = 6;

UPDATE languages
SET rating = 2
where id = 7;

UPDATE languages
SET rating = 3
where id = 8;

UPDATE languages
SET answered = 1
WHERE language = 'Python' and language = 'Go';

SELECT * FROM languages 
WHERE answer LIKE '200 OK' and answer LIKE 'Lambda';


 
