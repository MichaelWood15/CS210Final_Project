import sqlite3
con = sqlite3.connect("NBAOFFENSE.db")
cur = con.cursor()

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