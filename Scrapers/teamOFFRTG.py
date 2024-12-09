team_dict = {
    'TOR': 'Toronto Raptors',
    'DAL': 'Dallas Mavericks',
    'LAL': 'Los Angeles Lakers',
    'NOP': 'New Orleans Pelicans',
    'POR': 'Portland Trail Blazers',
    'CLE': 'Cleveland Cavaliers',
    'ORL': 'Orlando Magic',
    'HOU': 'Houston Rockets',
    'BOS': 'Boston Celtics',
    'MEM': 'Memphis Grizzlies',
    'UTA': 'Utah Jazz',
    'DEN': 'Denver Nuggets',
    'NYK': 'New York Knicks',
    'SAC': 'Sacramento Kings',
    'BKN': 'Brooklyn Nets',
    'MIN': 'Minnesota Timberwolves',
    'ATL': 'Atlanta Hawks',
    'GSW': 'Golden State Warriors',
    'OKC': 'Oklahoma City Thunder',
    'CHA': 'Charlotte Hornets',
    'LAC': 'LA Clippers',
    'MIL': 'Milwaukee Bucks',
    'SAS': 'San Antonio Spurs',
    'MIA': 'Miami Heat',
    'CHI': 'Chicago Bulls',
    'PHX': 'Phoenix Suns',
    'IND': 'Indiana Pacers',
    'DET': 'Detroit Pistons',
    'WAS': 'Washington Wizards',
    'PHI': 'Philadelphia 76ers'
}

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
    file.write('offensiveRating\n')


    for i in range(len(team)):
        file.write(team_dict[team[i]] + ',')
        file.write(offensiveRating[i] + "\n")

    






