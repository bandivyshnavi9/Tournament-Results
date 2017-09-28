******************************************************
* 	Author : Vyshnavi Bandi                          *
* 	Project : Tournament Database                    *
******************************************************

This is an extra option project folder. I  implemented  for odd number of players.

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
5. Type create database tournament_extras(database_name)
6. Exit from psql using (\q or CTRL+D)
7. Type psql tournament_extras(database_name)
8. To import the structures of tables and view's(\i tournament.sql)
9. To run the python file exit from psql using (\q or CTRL+D)
10. Now run tournament_test.py



RESULTS:

This table contains 9 players. Thus, first player is 'bye'.
The below table is playerstanding

 playerid |    playername     | wins | matches
----------+-------------------+------+---------
      180 | Twilight Sparkle  |    1 |       1
      181 | Fluttershy        |    0 |       0
      182 | Applejack         |    0 |       0
      183 | Pinkie Pie        |    0 |       0
      184 | Rarity            |    0 |       0
      185 | Rainbow Dash      |    0 |       0
      186 | Princess Celestia |    0 |       0
      187 | Princess Luna     |    0 |       0
      188 | Princess Vyshnavi |    0 |       0


Remaining 8 players undergo swisspairing and reported matches between them
in test file.
The playerstanding results after first round

 playerid |    playername     | wins | matches
----------+-------------------+------+---------
      219 | Rainbow Dash      |    1 |       1
      217 | Pinkie Pie        |    1 |       1
      221 | Princess Luna     |    1 |       1
      214 | Twilight Sparkle  |    1 |       1
      215 | Fluttershy        |    1 |       1
      222 | Princess Vyshnavi |    0 |       1
      216 | Applejack         |    0 |       1
      218 | Rarity            |    0 |       1
      220 | Princess Celestia |    0 |       1