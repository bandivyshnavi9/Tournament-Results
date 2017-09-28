******************************************************
* 	Author : Vyshnavi Bandi                          *
* 	Project : Tournament Database                    *
******************************************************


This project consists of
1. tournament.py: which contains all methods to be implemented
				  on the database.
2. tournament.sql: This file contains the structures of View's
					and table.
3. tournament_test.py: This file is used to test tournament.py.


Steps to run this project:
1. In vagrant file location,Open the git bash terminal.
2. Type vagrant ssh.
3. Change the path to tournament folder (cd /vagrant/Projectfoldername)
4. Type psql
5. Type create database tournament(database_name)
6. Exit from psql using (\q or CTRL+D)
7. Type psql tournament(database_name)
8. To import the structures of tables and view's(\i tournament.sql)
9. To run the python file exit from psql using (\q or CTRL+D)
10. Now run tournament_test.py

