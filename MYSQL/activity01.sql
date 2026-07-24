CREATE TABLE supplier (
    SNO VARCHAR(10) PRIMARY KEY,
    SNAME VARCHAR(50),
    CITY VARCHAR(50)
);

INSERT INTO supplier (SNO, SNAME, CITY) VALUES
('S1', 'Smith', 'London'),
('S2', 'Jones', 'Paris'),
('S3', 'Blake', 'Paris'),
('S4', 'Clarke', 'London'),
('S5', 'Adams',  'Athens');

SELECT * FROM supplier
WHERE CITY="Athens";