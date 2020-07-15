-- creates table id_not_null on MySQL server
-- table has id and name, where id has default value 1 if missing
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
