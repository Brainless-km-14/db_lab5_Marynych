SELECT * FROM year;
CREATE TABLE test_data AS SELECT * FROM year;
DELETE FROM test_data;

DO $$
  DECLARE
     year   year.year%TYPE;
     award$ year.award$%TYPE;
	 city_id year.city_id%TYPE;
	 id year.id%TYPE;
  BEGIN
  	 year := 2023;
	 award$ :=50000;
	 
 	 FOR counter IN 1..20
		 LOOP
			 INSERT INTO test_data(year,award$,city_id,id)
			 VALUES (year + counter, award$ + counter * 1000,random()+1,random()*3+1);
		 END LOOP;
  END;
  $$
 
SELECT * FROM test_data;