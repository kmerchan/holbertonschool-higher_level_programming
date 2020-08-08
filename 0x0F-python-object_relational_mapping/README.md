# 0x0F-python-object_relational_mapping
This directory contains initial work with MySQLdb and SQLALchemy:

0. Writing a script that lists all states in ascending order from the database using 3 arguments: username, password, database name, and using MySQLdb module
1. Writing a script that lists all states in ascending order with a name starting with N from database using same arguments and module as in task 0
2. Writing a script that takes in an argument and displays all values in the states table of a database where the name matches the given argument, in ascending order, using format
3. Repeat task 2, but ensure the script is safe from MySQL injections
4. Writing a script to list all cities from database in ascending order using MySQLdb and using execute() only once
5. Writing a script that takes in the name of a state as an argument and lists all cities of that state using MySQLdb and using execute() only once
6. Writing a python file that contains the class definition of a State and instance Base, where State inherits from Base, and using SQLAlchemy module
7. Writing a script that lists all State objects in ascending order from the database using SQLALchemy
8. Writing a script that prints the first State object from the database using SQLAlchemy without fetching all states from the database before displaying the result
9. Writing a script that lists all State objects that contain the letter 'a' from the database using SQLAlchemy
10. Writing a script that prints the State object with the name matching the argument passed to the script using SQLAlchemy
11. Writing a script that adds the State object 'Louisiana' to the database using SQLAlchemy and print the new states.id after creation
12. Writing a script that change the name of a State object in the database using SQLAlchemy and using id number
13. Writing a script that deletes all State object with a name containing the letter 'a' from a database using SQLAlchemy
14. Writing a Python file that contains the class definition of a City, which also inherits from Base, using MySQLAlchemy and write a script that prints all City objects from the database using MySQL
