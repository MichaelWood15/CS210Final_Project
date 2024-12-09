"""

for our ML, we are going to be doing a K-means Clustering with teams offensive rating and there best players offensive stats
almost all Championship teams in the past have had a good offense with an elite best player. To find these stats, we are going
to query each teams best player's stats with constraints on fg%  and games played, along with there offensive rating, and we are
going to group offenses into clusters where the x axis is offensive rating and the y axis is the effectiveness of there best player
on offense

we can calculate the teams best offensive player by taking into account there ppg and fg percentage. for simplicity purposes, we will 
use the player that averaged the most ppg AND shot over 43% from the field


"""
import sqlite3

con = sqlite3.connect("NBAOFFENSE.db")
cur = con.cursor()

# We want every teams offensive rating, and best player

playerQuery = '''
SELECT Team, playerName, ppg
FROM NBAPLAYERS
WHERE fgPercentage > 43
AND playerName IN (
    SELECT playerName
    FROM NBAPLAYERS
    WHERE fgPercentage > 43
    GROUP BY Team
    HAVING ppg = MAX(ppg)
);
'''
teamQuery = '''
SELECT Name, ORT
FROM NBATEAMS
'''
# Execute the query
cur.execute(playerQuery)

# Fetch the result
bestPlayer = cur.fetchall()

Team = {}
if bestPlayer:
    for row in bestPlayer:
    
        team, player_name, ppg = row
        Team[team] = [(player_name, ppg)]

        # print(f"Team: {team}, Player: {player_name}, PPG: {ppg}")
else:
    print("No players found meeting the criteria.")


cur.execute(teamQuery)
teamORT = cur.fetchall()

for row in teamORT:
    team, ORT = row
    Team[team].append(ORT)

for element in Team:
    print(element , Team[element])

con.close()


