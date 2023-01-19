from queue import Empty
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By    

def scrape_fantasy_online_html():
    json_file = open("C:/Users/Nick/Unity/Fantasy Online/Wiki/fo-wiki/fo-wiki.com/.content.X7ZfEtZn/structure_jsons/edited/skill_edited.json")
    skill_json = json.load(json_file)
    driver = webdriver.Chrome(executable_path='C:/Users/Work/Git/chromedriver/chromedriver.exe')
    for item in sorted(skill_json["skills"], key=get_id):
        if("display" in item["name"]):
            get_display_files(item, driver)
        
    json_file.close()
def get_display_files(skill, driver):
    driver.get("file://C:/Users/Nick/Unity/Fantasy Online/Wiki/fo-wiki/fo-wiki.com/.content.X7ZfEtZn/html/" + skill["filename"])
    try:
        print(
            '{ "id": "' + skill["name"].split("_")[0]
            + '", "name": "' + driver.find_elements(By.TAG_NAME, "td")[1].text.split("[")[0].strip()
            + '", "rank": "' + driver.find_elements(By.TAG_NAME, "td")[9].text.strip()
            + '", "requirments": "' + driver.find_elements(By.TAG_NAME, "td")[13].text.strip().replace("\n", " ")
            + '", "sp_cost": "' + driver.find_elements(By.TAG_NAME, "td")[7].text.strip()
            + '", "damage": "' + driver.find_elements(By.TAG_NAME, "td")[5].text.strip()
            + '", "buy_price": "' + driver.find_elements(By.TAG_NAME, "td")[15].text.strip()
            + '", "obtained_from": ' + get_obtained_from(driver)
            +  ', "description": "' + driver.find_elements(By.TAG_NAME, "td")[3].text.strip().replace("\n", " ").replace('"', '\\"')
            + '", "note": "' + driver.find_elements(By.TAG_NAME, "td")[17].text.replace('"', '\\"')
            + '" },'
        )
    except:
        print('{ "id": "' + skill["name"].split("_")[0] + '", "name": "empty_item" },')
def get_obtained_from(driver):
    drops_str = ''
    drops = driver.find_elements(By.TAG_NAME, "td")[11].find_elements(By.TAG_NAME, "a")
    for drop in drops:
        drop_id = drop.get_attribute("href").split("id=")[-1]
        drop_name = drop_name = drop.text.strip()
        if drop_name:
            if drops_str:
                drops_str += ', '
            drops_str += '{ "id": "%s", "name": "%s" }'%(drop_id, drop_name)
    return "[" + drops_str + "]"

def get_id(json):
    return int(json["name"].split("_")[0])

if __name__ == "__main__":
    scrape_fantasy_online_html()
