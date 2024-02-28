use alumnes;

CREATE TABLE students(
    StudentID int not null AUTO_INCREMENT,
    FirstName varchar(100) NOT NULL,
    Surname varchar(100) NOT NULL,
    PRIMARY KEY (StudentID)
);

INSERT INTO students (FirstName, Surname) VALUES ('Tony', 'Stark');
INSERT INTO students (FirstName, Surname) VALUES ('Steve', 'Rogers');
INSERT INTO students (FirstName, Surname) VALUES ('Bruce', 'Banner');
INSERT INTO students (FirstName, Surname) VALUES ('Natasha', 'Romanoff');
INSERT INTO students (FirstName, Surname) VALUES ('Thor', 'Odinson');
INSERT INTO students (FirstName, Surname) VALUES ('Peter', 'Parker');
INSERT INTO students (FirstName, Surname) VALUES ('Wanda', 'Maximoff');
INSERT INTO students (FirstName, Surname) VALUES ('Scott', 'Lang');
INSERT INTO students (FirstName, Surname) VALUES ('Carol', 'Danvers');
INSERT INTO students (FirstName, Surname) VALUES ('T''Challa', 'Wakanda');
