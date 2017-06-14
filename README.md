# dbbackup

Author: Sean Themar

Introduction:
dbbackup is a script that creates .csv backup files of a MS SQL Server Database's tables.
The script creates a folder with the current date and creates a .csv for each table in the 
database.  If the folder already exists, the files are overwritten.

Prerequisites:
  - Python 3.X
  - MS SQL Server

Install and Run:
	- Create a directory to store dbbackup.py
  - Edit script to change SERVER name(line 14) and DATABASE name(line 17 ex: database.INFORMATION_SCHEMA.TABLES)
  - Run script through cmd.exe or by double clicking dbbackup.py
  - Script will prompt for the users database name, user, and password
  
Bugs:
  - Cannot handle varbinary
  - Change line 17 so users don't have to change database name
