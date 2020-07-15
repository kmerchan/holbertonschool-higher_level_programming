-- creates table unique_id on MySQL server
-- table has id and name, where id must be unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
