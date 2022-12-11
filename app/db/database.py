import pyodbc

connect_database = pyodbc.connect(
  r'Driver={SQL Server};Server=DESKTOP-DNS857G;Database=db rgr1;Trusted_Connection=yes;')
cursor = connect_database.cursor()
