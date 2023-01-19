from queue import Empty
import time
import json
from selenium import webdriver    

def scrape_fantasy_online_html():
    driver = webdriver.Chrome(executable_path='C:/Users/Work/Git/chromedriver/chromedriver.exe')
    json_file = open("C:/Users/Nick/Unity/Fantasy Online/Wiki/fo-wiki/fo-wiki.com/.content.X7ZfEtZn/structure_jsons/edited/npc_edited.json")
    npc_json = json.load(json_file)
    for npc in npc_json["npcs"]:
        if("display" in npc["name"]):
            get_display_files(npc, driver)
        
    json_file.close()
def get_display_files(npc, driver):
    driver.get("file://C:/Users/Nick/Unity/Fantasy Online/Wiki/fo-wiki/fo-wiki.com/.content.X7ZfEtZn/html/" + npc["filename"])
    print(
           '{ "id": "' + npc["name"].split("_")[0]
        + '", "name": "' + driver.find_elements_by_tag_name("td")[1].text.split("[")[0].strip()
        + '", "coordinates": "' + driver.find_elements_by_tag_name("td")[5].text
        + '", "drops": ' + get_display_drops(driver)
        +  ', "quests": ' + get_display_quests(driver)
        +  ', "note": "' + driver.find_elements_by_tag_name("td")[7].text.replace('"', '\\"')
        + '" },'
    )

def get_display_drops(driver):
    drops_str = ''
    drops = driver.find_elements_by_tag_name("td")[3].find_elements_by_tag_name("a")
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
    drops = driver.find_elements_by_tag_name("td")[3].find_elements_by_tag_name("a")
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
