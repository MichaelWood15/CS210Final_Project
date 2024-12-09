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

            print(name, team, ppg, gp, fgPercentage)

        line = playerStats.readline()