import sqlite3

# create connection w/ sqlite3
con = sqlite3.connect("NBAOFFENSE.db")
cur = con.cursor()

cur.execute('''
    CREATE TABLE if NOT EXISTS NBAPLAYERS(
        playerName varChar(100) PRIMARY KEY,
        Team varChar(50),
        ppg DECIMAL(2,2),
        gp INT,
        fgPercentage DECIMAL(2,2))''')


# fill out table using the CSVs created

with open('CSVs/playerStatistics.csv' , 'r') as playerStats:

    line = playerStats.readline()
    switch = False
    while line is not None and len(line) > 2:
        if not switch:
            switch = True
        else:
            line = line.split(",")
            name = line[0]
            team = line[1]
            ppg = line[2]
            gp = line[3]
            fgPercentage = line[4]


            cur.execute('''
            INSERT INTO NBAPLAYERS (playerName, Team, ppg, gp, fgPercentage)
            VALUES (?, ?, ?, ?, ?)''', 
            (name, team, ppg, gp, fgPercentage))
            con.commit()  # Commit the transaction to the database


        line = playerStats.readline()

con.close()




