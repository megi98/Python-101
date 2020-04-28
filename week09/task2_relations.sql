--1--
SELECT name FROM STARSIN
  JOIN MOVIESTAR on STARSIN.starname = MOVIESTAR.name
  where STARSIN.movietitle = 'Terms of Endearment' AND MOVIESTAR.gender = 'M';

--2--
SELECT starname FROM STARSIN
  JOIN MOVIE on STARSIN.movietitle = MOVIE.title
  WHERE MOVIE.studioname = 'MGM' AND STARSIN.movieyear = 1995;

--3--
ALTER TABLE STUDIO
  add COLUMN presidentname VARCHAR(35);

UPDATE STUDIO
  set presidentname = 'President1'
  WHERE name = 'MGM';
  
UPDATE STUDIO
  set presidentname = 'President2'
  WHERE name = 'USA Entertainm.';

SELECT presidentname FROM STUDIO
  WHERE name = 'MGM';