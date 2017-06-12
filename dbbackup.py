import pyodbc
import os
import time
import csv
import binascii
import getpass


dbName = input('Enter database name: ')
user = input('Enter username: ')
pw = getpass.getpass('Enter password: ')
newpath = r"C:\Users\CCSDeveloper\Documents\Database Backups"+time.strftime(r"\%m%d%Y")
tableList = []
conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=ADD YOUR SERVER HERE;DATABASE='+dbName+';UID='+user+';PWD='+pw)
cursor = conn.cursor()

cursor.execute("SELECT * FROM DATABASENAME.INFORMATION_SCHEMA.TABLES")
row = cursor.fetchone()

#Add all the table names to a list
while row:
	tableList.append(row[2])
	row = cursor.fetchone()
	
#Write to or create a new directory.
#Execute SELECT statement on each table
#in our table list.
#BUGS:-Cannot handle varbinary
if os.path.exists(newpath):
	for tab in tableList:
		cursor.execute("SELECT * FROM "+tab)
		row = cursor.fetchone()
		#with open(newpath+'\\'+tab+'.txt', 'w', newline='') as txtfile:
		#	while row:
		#		txtfile.write(str(row))
		#		row = cursor.fetchone()
		with open(newpath+'\\'+tab+'.csv', 'w', newline='') as csvfile:
			tabwriter = csv.writer(csvfile, delimiter=',')
			tabwriter.writerow(i[0] for i in cursor.description)
			while row:
				tabwriter.writerow(row)
				row = cursor.fetchone()
else:
	os.makedirs(newpath)
	for tab in tableList:
		cursor.execute("SELECT * FROM "+tab)
		row = cursor.fetchone()
		#with open(newpath+'\\'+tab+'.txt', 'w', newline='') as txtfile:
		#	while row:
		#		txtfile.write(str(row))
		#		row = cursor.fetchone()
		with open(newpath+'\\'+tab+'.csv', 'w', newline='') as csvfile:
			tabwriter = csv.writer(csvfile, delimiter=',')
			tabwriter.writerow(i[0] for i in cursor.description)
			while row:
				tabwriter.writerow(row)
				row = cursor.fetchone()




