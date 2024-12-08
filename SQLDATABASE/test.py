import os
print(os.getcwd())
with open ('CSVs/shotDietByTeam.csv' , 'r') as shotDiet, open ('CSVs/teamOffensiveRating.csv', 'r') as ORT:
    for i in range(30):

        count = 0

        switchone = False
        switchtwo = False
        for i in range(31):
            print(i)
            if switchone:
                line1 = shotDiet.readline()
                
                # Split the line1
                line1 = line1.split(',')
                print(line1)
                
                # Extract values to put into the database
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
                
                # Print all values for verification
                print(f"Team: {teamOne}")
                print(f"Layup Made: {layupMade}, Layup Attempted: {layupAtt}, Layup Percentage: {layupPercentage}")
                print(f"Floater Made: {floaterMade}, Floater Attempted: {floaterAtt}, Floater Percentage: {floaterPercentage}")
                print(f"Short Midrange Made: {shortMidrangeMade}, Short Midrange Attempted: {shortMidrangeAtt}, Short Midrange Percentage: {shortMidrangePercentage}")
                print(f"Midrange Made: {midrangeMade}, Midrange Attempted: {midrangeAtt}, Midrange Percentage: {midrangePercentage}")
                print(f"Long Midrange/Three Made: {longMidrangeOrThreeMade}, Long Midrange/Three Attempted: {longMidrangeOrThreeAtt}, Long Midrange/Three Percentage: {longMidrangeOrThreePercentage}")
                print(f"Three Made: {threeMade}, Three Attempted: {threeAtt}, Three Percentage: {threePercentage}")
                print("-" * 50)  # Separator for clarity
                
            else: 
                switchone = True
                line1 = shotDiet.readline()



            if switchtwo:
                line2 = ORT.readline()
                line2 = line2.split(',')
                teamtwo = line2[0]
                OFFRTG = line2[1]
                
                # Print values from ORT file
                print(f"Team: {teamtwo}, Offensive Rating (ORT): {OFFRTG}")
            else: 
                switchtwo = True
                line2 = ORT.readline()






       