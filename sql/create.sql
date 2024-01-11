-- CREATE TABLE student_groups(id INT PRIMARY KEY,
-- 					groupName VARCHAR(50) NOT NULL,
-- 					facultyId INT);
CREATE TABLE students(id INT PRIMARY KEY,
					  firstName VARCHAR(50) NOT NULL,
                      lastName VARCHAR(50) NOT NULL,
                      birthDate DATE NOT NULL,
                      Grands FLOAT,
                      email VARCHAR(50) NOT NULL,
                      groupId INT REFERENCES student_groups(id));
			