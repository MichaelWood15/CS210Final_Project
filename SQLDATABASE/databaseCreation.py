import sqlite3

con = sqlite3.connect("NBAOFFENSE.db")
cur = con.cursor()

cur.execute(
'''CREATE TABLE if NOT EXISTS NBATEAMS
(Name varchar(30) PRIMARY KEY, 
ORT DECIMAL(3,2), layupmade DECIMAL (2,2), 
layupatt DECIMAL (2,2), 
layuppercentage DECIMAL (2,2), 
floatermade DECIMAL (2,2), 
floateratt DECIMAL (2,2), 
floaterpercentage DECIMAL (2,2), 
shortmidrangemade DECIMAL (2,2), 
shortmidrangeatt DECIMAL (2,2), 
shortmidrangepercentage DECIMAL (2,2),
 midrangemade DECIMAL (2,2), 
 midrangeatt DECIMAL (2,2), 
 midrangepercentage DECIMAL (2,2), 
 longmidrangeorthreemade DECIMAL (2,2), 
 longmidrangeorthreeatt DECIMAL (2,2), 
 longmidrangeorthreepercentage DECIMAL (2,2), 
 threemade DECIMAL (2,2), threeatt DECIMAL (2,2), 
 threepercentage DECIMAL (2,2))''')

