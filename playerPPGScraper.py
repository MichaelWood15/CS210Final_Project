from playwright.sync_api import sync_playwright


url = 'https://www.nba.com/stats/players/traditional?Season=2023-24'


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    team = []
    player = []
    ppg = []
    gp = []
    fgPercantage = []

    for i in range(11):

        for i in range(1,51):
            player.append(page.locator("//table[@class='Crom_table__p1iZz']//tbody[@class='Crom_body__UYOcU']//tr[" + str(i) + "]//td[2]").text_content())
            team.append(page.locator("//table[@class='Crom_table__p1iZz']//tbody[@class='Crom_body__UYOcU']//tr[" + str(i) + "]//td[3]").text_content())
            ppg.append(page.locator("//table[@class='Crom_table__p1iZz']//tbody[@class='Crom_body__UYOcU']//tr[" + str(i)+"]//td[9]").text_content())
            gp.append(page.locator("//table[@class='Crom_table__p1iZz']//tbody[@class='Crom_body__UYOcU']//tr[" + str(i)+"]//td[5]").text_content())
            fgPercantage.append(page.locator("//table[@class='Crom_table__p1iZz']//tbody[@class='Crom_body__UYOcU']//tr[" + str(i)+"]//td[12]").text_content())

        page.locator("//button[@title='Next Page Button']").click()

    rows = page.locator("//table[@class='Crom_table__p1iZz']//tbody[@class='Crom_body__UYOcU']//tr").count()

    for i in range(1,rows+1):
        player.append(page.locator("//table[@class='Crom_table__p1iZz']//tbody[@class='Crom_body__UYOcU']//tr[" + str(i) + "]//td[2]").text_content())
        team.append(page.locator("//table[@class='Crom_table__p1iZz']//tbody[@class='Crom_body__UYOcU']//tr[" + str(i) + "]//td[3]").text_content())
        ppg.append(page.locator("//table[@class='Crom_table__p1iZz']//tbody[@class='Crom_body__UYOcU']//tr[" + str(i)+"]//td[9]").text_content())
        gp.append(page.locator("//table[@class='Crom_table__p1iZz']//tbody[@class='Crom_body__UYOcU']//tr[" + str(i)+"]//td[5]").text_content())
        fgPercantage.append(page.locator("//table[@class='Crom_table__p1iZz']//tbody[@class='Crom_body__UYOcU']//tr[" + str(i)+"]//td[12]").text_content())


    
    return player , team, ppg, gp, fgPercantage
    

with sync_playwright() as playwright:
    player , team, ppg, gp, fgPercantage = run(playwright)



with open('playerStatistics.csv' , 'w') as file:
    file.write('Player,')
    file.write('Team,')
    file.write('ppg,')
    file.write('gp,')
    file.write('fgPercentage,\n')

    for i in range(len(player)):
        file.write(player[i] + ",")
        file.write(team[i] + ",")
        file.write(ppg[i] + ",")
        file.write(gp[i] + ",")
        file.write(fgPercantage[i] + ",\n")




    

    
        