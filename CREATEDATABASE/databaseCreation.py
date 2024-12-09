import sqlite3

# create connection w/ sqlite3
con = sqlite3.connect("NBAOFFENSE.db")
cur = con.cursor()

# Create NBA teams database if it doesn't exist already
cur.execute('''
CREATE TABLE if NOT EXISTS NBATEAMS
(Name varchar(30) PRIMARY KEY, 
ORT DECIMAL(3,2), 
layupmade DECIMAL(2,2), 
layupatt DECIMAL(2,2), 
layuppercentage DECIMAL(2,2), 
floatermade DECIMAL(2,2), 
floateratt DECIMAL(2,2), 
floaterpercentage DECIMAL(2,2), 
shortmidrangemade DECIMAL(2,2), 
shortmidrangeatt DECIMAL(2,2), 
shortmidrangepercentage DECIMAL(2,2),
midrangemade DECIMAL(2,2), 
midrangeatt DECIMAL(2,2), 
midrangepercentage DECIMAL(2,2), 
longmidrangeorthreemade DECIMAL(2,2), 
longmidrangeorthreeatt DECIMAL(2,2), 
longmidrangeorthreepercentage DECIMAL(2,2), 
threemade DECIMAL(2,2), 
threeatt DECIMAL(2,2), 
threepercentage DECIMAL(2,2))''')

# fill out table using the CSVs created
import os
print(os.getcwd())

with open('CSVs/shotDietByTeam.csv', 'r') as shotDiet, open('CSVs/teamOffensiveRating.csv', 'r') as ORT:
    print(shotDiet)
    
    count = 0
    switchone = False
    switchtwo = False

    for i in range(31):
        if switchone:
            line1 = shotDiet.readline()
            line1 = line1.split(',')
            
            if len(line1) > 2: 
                teamOne = line1[0]
                layupMade = line1[1]
                layupAtt = line1[2]
                layupPercentage = line1[3]
                floaterMade = line1[4]
                floaterAtt = line1[5]
                floaterPercentage = line1[6]
                shortMidrangeMade = line1[7]
                shortMidrangeAtt = line1[8]
                shortMidrangePercentage = line1[9]
                midrangeMade = line1[10]
                midrangeAtt = line1[11]
                midrangePercentage = line1[12]
                longMidrangeOrThreeMade = line1[13]
                longMidrangeOrThreeAtt = line1[14]
                longMidrangeOrThreePercentage = line1[15]
                threeMade = line1[16]
                threeAtt = line1[17]
                threePercentage = line1[18]
                
                
                
        else: 
            switchone = True
            line1 = shotDiet.readline()

        if switchtwo:
            line2 = ORT.readline()
            line2 = line2.split(',')

            while(len(line2) > 1 and line2[0] != teamOne): 

                line2 = ORT.readline().split(',')
            teamtwo = line2[0]
            OFFRTG = line2[1]
            ORT.seek(0)
            
        else: 
            switchtwo = True
            line2 = ORT.readline()

        if i != 0:
            print('here')

            # Use placeholders to avoid SQL injection and fix string formatting
            cur.execute('''
            INSERT INTO NBATEAMS (Name, ORT, layupmade, layupatt, layuppercentage, floatermade, floateratt, floaterpercentage, 
            shortmidrangemade, shortmidrangeatt, shortmidrangepercentage, midrangemade, midrangeatt, midrangepercentage, 
            longmidrangeorthreemade, longmidrangeorthreeatt, longmidrangeorthreepercentage, threemade, threeatt, threepercentage)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
            (teamOne, OFFRTG, layupMade, layupAtt, layupPercentage, floaterMade, floaterAtt, floaterPercentage, 
            shortMidrangeMade, shortMidrangeAtt, shortMidrangePercentage, midrangeMade, midrangeAtt, midrangePercentage, 
            longMidrangeOrThreeMade, longMidrangeOrThreeAtt, longMidrangeOrThreePercentage, threeMade, threeAtt, threePercentage))

            con.commit()  # Commit the transaction to the database

cur.execute("SELECT * FROM NBATEAMS")
rows = cur.fetchall()

# Print column names (optional)
columns = [description[0] for description in cur.description]
print("\t".join(columns))  # Print the column names as a header

# Print each row
for row in rows:
    print("\t".join(str(cell) for cell in row))

# Step 5: Commit and close the connection
con.commit()
con.close()