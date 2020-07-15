-- creates table unique_id on MySQL server
-- table has id and name, where id must be unique
CREATE TABLE IF NOT EXISTS unique_id (UNIQUE KEY(id INT DEFAULT 1), name VARCHAR(256));
