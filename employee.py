import sqlite3

conn = sqlite3.connect('employee.db')
print('Opened database successfully')

conn.execute('CREATE TABLE information (EmpID VARCHAR(200), EmpName VARCHAR(200), EmpGender VARCHAR(200), EmpPhone VARCHAR(10), EmpBdate DATE);')
print('Table created successfully')

conn.close()
