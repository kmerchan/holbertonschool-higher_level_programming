-- creates database hbtn_0d_usa and table cities
-- table has id, state_id, and name
-- id is primary key, state_id is foreign key, and name can't be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT PRIMARY KEY, state_id INT FOREIGN KEY REFERENCES state(id), name VARCHAR(256) NOT NULL);
