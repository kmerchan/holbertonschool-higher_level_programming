-- creates table force_name on MySQL server
-- table has id and name, where name can't be null
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
