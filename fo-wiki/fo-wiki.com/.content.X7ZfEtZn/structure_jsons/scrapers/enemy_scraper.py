from queue import Empty
import time
import json
from selenium import webdriver    

def scrape_fantasy_online_html():
    driver = webdriver.Chrome(executable_path='C:/Users/Work/Git/chromedriver/chromedriver.exe')
    json_file = open("C:/Users/Nick/Unity/Fantasy Online/Wiki/fo-wiki/fo-wiki.com/.content.X7ZfEtZn/structure_jsons/edited/enemy_edited.json")
    enemy_json = json.load(json_file)
    for enemy in enemy_json["enemies"]:
        if("display" in enemy["name"]):
            get_display_files(enemy, driver)
        
    json_file.close()
def get_display_files(enemy, driver):
    driver.get("file://C:/Users/Nick/Unity/Fantasy Online/Wiki/fo-wiki/fo-wiki.com/.content.X7ZfEtZn/html/" + enemy["filename"])
    print(
           '{ "id": "' + enemy["name"].split("_")[0]
        + '", "name": "' + driver.find_elements_by_tag_name("td")[1].text.split("[")[0].strip()
        + '", "race": "' + driver.find_elements_by_tag_name("td")[3].text
        + '", "hp": "' + driver.find_elements_by_tag_name("td")[5].text
        + '", "xp": "' + driver.find_elements_by_tag_name("td")[7].text
        + '", "level": "' + driver.find_elements_by_tag_name("td")[9].text
        + '", "sp": "' + driver.find_elements_by_tag_name("td")[11].text
        + '", "damage": "' + driver.find_elements_by_tag_name("td")[13].text
        + '", "respawn_time": "' + driver.find_elements_by_tag_name("td")[15].text
        + '", "aggro": "' + driver.find_elements_by_tag_name("td")[17].text
        + '", "boss": "' + driver.find_elements_by_tag_name("td")[19].text
        + '", "attack_Speed": "' + driver.find_elements_by_tag_name("td")[21].text
        + '", "walk_speed": "' + driver.find_elements_by_tag_name("td")[23].text
        + '", "size": "' + driver.find_elements_by_tag_name("td")[25].text
        + '", "ranged_attack": "' + driver.find_elements_by_tag_name("td")[27].text
        + '", "coordinates": "' + driver.find_elements_by_tag_name("td")[29].text
        + '", "drops": ' + get_display_drops(driver)
        +  ', "quests": ' + get_display_quests(driver)
        +  ', "note": ' + driver.find_elements_by_tag_name("td")[37].text
        + '" },'
    )

def get_display_drops(driver):
    drops_str = ''
    drops = driver.find_elements_by_tag_name("td")[31].find_elements_by_tag_name("a")
    for drop in drops:
        drop_id = drop.get_attribute("href").split("id=")[-1]
        drop_name = drop_name = drop.text.strip()
        if not drop_name:
            if drops_str:
                drops_str += ', '
            drop_name = drop.find_element_by_tag_name("img").get_attribute("title")
            drops_str += '{ "id": "%s", "name": "%s" }'%(drop_id, drop_name)
    return "[" + drops_str + "]"

def get_display_quests(driver):
    drops_str = ''
    drops = driver.find_elements_by_tag_name("td")[31].find_elements_by_tag_name("a")
    for drop in drops:
        drop_id = drop.get_attribute("href").split("id=")[-1]
        drop_name = drop_name = drop.text.strip()
        if drop_name:
            if drops_str:
                drops_str += ', '
            drops_str += '{ "id": "%s", "name": "%s" }'%(drop_id, drop_name)
    return "[" + drops_str + "]"


if __name__ == "__main__":
    scrape_fantasy_online_html()
