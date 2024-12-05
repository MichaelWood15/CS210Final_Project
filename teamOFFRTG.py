from playwright.sync_api import sync_playwright
url = "https://www.nba.com/stats/teams/advanced?Season=2023-24"



def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    team = []
    offensiveRating = []

    teamCount = 30

    for i in range(1, teamCount+1):
        team.append(page.locator("//tbody[@class='Crom_body__UYOcU']//tr[" + str(i) + "]//td[2]").text_content())
        offensiveRating.append(page.locator("//tbody[@class='Crom_body__UYOcU']//tr[" + str(i) + "]//td[7]").text_content())

    return team, offensiveRating



with sync_playwright() as playwright:
    team, offensiveRating = run(playwright)
    
# for i in range(len(team)):
#     print(team[i])
#     print(offensiveRating[i])

with open('teamOffensiveRating.csv' , 'w') as file:
    file.write('Team,')
    file.write('offensiveRating,\n')


    for i in range(len(team)):
        file.write(team[i] + ',')
        file.write(offensiveRating[i] + ",\n")

    




