-- creates database hbtn_0d_2 and user user_0d_2
-- user_0d_2 should hava password user_0d_2_pwd and only SELECT privilege
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER user_0d_2 IDENTIFIED BY user_0d_2_pwd;
GRANT SELECT PRIVILEGES ON hbnt_0d_2.* TO user_0d_2;
