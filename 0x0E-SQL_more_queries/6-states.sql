-- creates database hbtn_0d_usa and table states
-- table has id and name, where id is primary key and name can't be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
