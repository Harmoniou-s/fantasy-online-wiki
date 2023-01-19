from queue import Empty
import time
import json
from selenium import webdriver    

def scrape_fantasy_online_html(driver):
    json_file = open("C:/Users/Nick/Unity/Fantasy Online/Wiki/fo-wiki/fo-wiki.com/.content.X7ZfEtZn/structure_jsons/edited/quest_edited.json")
    quest_json = json.load(json_file)
    for quest in quest_json["quests"]:
        if("display" in quest["name"]):
            get_display_files(quest, driver)

def get_display_files(quest, driver):
    driver.get("file://C:/Users/Nick/Unity/Fantasy Online/Wiki/fo-wiki/fo-wiki.com/.content.X7ZfEtZn/html/" + quest["filename"])
    print(
           '{ "id": "' + quest["name"].split("_")[0]
        + '", "name": "' + driver.find_elements_by_tag_name("td")[1].text.split("[")[0].strip()
        + '", "start_npc": ' + get_start_npc(driver)
        + ', "type": "' + driver.find_elements_by_tag_name("td")[5].text
        + '", "xp_reward": "' + driver.find_elements_by_tag_name("td")[7].text
        + '", "coin_reward": "' + driver.find_elements_by_tag_name("td")[9].text
        + '", "summary": "' + driver.find_elements_by_tag_name("td")[11].text
        + '", "details": "' + parse_details(driver)
        + '", "note": "' + driver.find_elements_by_tag_name("td")[15].text
        + '" },'
    )

def get_start_npc(driver):
    npc = driver.find_elements_by_tag_name("td")[3].find_element_by_tag_name("a")
    npc_id = npc.get_attribute("href").split("id=")[-1]
    npc_name = npc.find_element_by_tag_name("img").get_attribute("title")
    return '{ "id": "%s", "name": "%s" }'%(npc_id, npc_name)

def parse_details(driver):
    a_tags = driver.find_elements_by_tag_name("td")[13].find_elements_by_tag_name("a")
    for a_tag in a_tags:
        driver.execute_script("arguments[0].innerText = '%s'"%parse_a_tag(a_tag), a_tag)

    imgs = driver.find_elements_by_tag_name("td")[13].find_elements_by_tag_name("img")
    for img in imgs:
        driver.execute_script("arguments[0].innerText = '%s'"%parse_set_content(img), img)

    return driver.find_elements_by_tag_name("td")[13].text.replace("\n", " \\n ")
        
def parse_a_tag(a_tag):
    tag_id = a_tag.get_attribute("href").split("id=")[-1]
    tag_name = a_tag.text.strip()
    a_href = a_tag.get_attribute("href")
    tag_type = ""
    
    if("bestiary" in a_href):
        tag_type = "enemy"
    elif ("npc" in a_href):
        tag_type = "npc"
    elif ("quest" in a_href):
        tag_type = "quest"
    elif ("items" in a_href):
        tag_type = "items"

    if not tag_name:
        tag_name = a_tag.find_element_by_tag_name("img").get_attribute("title")

    return ('{ id: %s, type: %s, name: %s }'%(tag_id, tag_type, tag_name)).replace("'", '')

def parse_set_content(img):
        return img.get_attribute('onmouseover').replace("'", '').replace("<br />", " \\n ").replace("  ", " ")[17:-26]
        
    
if __name__ == "__main__":
    scrape_fantasy_online_html(webdriver.Chrome(executable_path='C:/Users/Work/Git/chromedriver/chromedriver.exe'))
