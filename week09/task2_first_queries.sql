--1--
SELECT address FROM STUDIO 
  WHERE name = 'MGM';

--2--
SELECT birthdate FROM MOVIESTAR 
  WHERE name = 'Kim Basinger';

--3--
SELECT name FROM MOVIEEXEC
  WHERE networth > 10000000;

--4--
SELECT name FROM MOVIESTAR 
  WHERE gender = 'M' OR address = 'Prefect Rd.';

--5--
INSERT INTO MOVIESTAR
  VALUES('Zahari Baharov', 'Sofia', 'M', '1980-08-12');

--6--
DELETE FROM STUDIO
  WHERE address LIKE '%5%';

--7--
UPDATE MOVIE
  set studioname = 'Fox'
  WHERE title LIKE '%star%';