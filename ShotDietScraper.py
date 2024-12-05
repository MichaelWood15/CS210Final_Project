from playwright.sync_api import sync_playwright
import time

url = 'https://www.nba.com/stats/teams/shooting?Season=2023-24'

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    shotTypes = []
    NshotTypes = page.locator("//tr[@class='Crom_colgroup__qYrzI']//th[@class='Crom_navy__bedHS']").count()
    time.sleep(1)
    for i in range(NshotTypes):
        shotTypes.append(page.locator("//tr[@class='Crom_colgroup__qYrzI']//th[@class='Crom_navy__bedHS']").nth(i).text_content())

    for x in shotTypes:print(x)


    Nteams = page.locator("//tbody[@class='Crom_body__UYOcU']//tr").count()
    time.sleep(1)
    shotDiet = {}
    


    # go through each row




    for row in range(Nteams):
        shotDiet[ page.locator("//tbody[@class='Crom_body__UYOcU']//tr" + "[" + (str(row + 1)) + "]//td[1]").text_content() ] = {}
        count = 2

        for element in shotTypes:
            
            (shotDiet[page.locator("//tbody[@class='Crom_body__UYOcU']//tr" + "[" + (str(row + 1)) + "]//td[1]").text_content() ])[element] = []
            #print(shotDiet)
            for i in range(3):
                shotDiet[ page.locator("//tbody[@class='Crom_body__UYOcU']//tr" + "[" + (str(row + 1)) + "]//td[1]").text_content() ][element].append(page.locator("//tbody[@class='Crom_body__UYOcU']//tr" + "[" + (str(row + 1)) + "]//td[" + str(count) + "]").text_content())
                count+=1

   

    return shotDiet, shotTypes

with sync_playwright() as playwright:
    shotDiet, shotTypes = run(playwright)




with open('shotDietByTeam.csv' , 'w') as out:
    
    #cols 
    out.write(',')
    for shot in shotTypes:
        out.write(shot + ' made,')  
        out.write(shot + ' attempted,')
        out.write(shot + ' percentage')  
    out.write('\n')

    for team in shotDiet:
        out.write(team + ',')
        for element in shotDiet[team]:
            for stat in shotDiet[team][element]:
                out.write(stat + ',')
        out.write('\n')

    
    
# added comment

