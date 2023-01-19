from queue import Empty
import time
import json
from selenium import webdriver    

def scrape_fantasy_online_html():
    json_file = open("C:/Users/Nick/Unity/Fantasy Online/Wiki/fo-wiki/fo-wiki.com/.content.X7ZfEtZn/structure_jsons/edited/item_edited.json")
    item_json = json.load(json_file)
    driver = webdriver.Chrome(executable_path='C:/Users/Work/Git/chromedriver/chromedriver.exe')
    for item in sorted(item_json["items"], key=get_id):
        if("display" in item["name"]):
            get_display_files(item, driver)
        
    json_file.close()
def get_display_files(item, driver):
    driver.get("file://C:/Users/Nick/Unity/Fantasy Online/Wiki/fo-wiki/fo-wiki.com/.content.X7ZfEtZn/html/" + item["filename"])
    try:
        print(
            '{ "id": "' + item["name"].split("_")[0]
            + '", "name": "' + driver.find_elements_by_tag_name("td")[1].text.split("[")[0].strip()
            + '", "class": "' + driver.find_elements_by_tag_name("td")[3].text.strip()
            + '", "buy_price": "' + driver.find_elements_by_tag_name("td")[5].text.strip()
            + '", "sell_price": "' + driver.find_elements_by_tag_name("td")[7].text.strip()
            + '", "required_level": "' + driver.find_elements_by_tag_name("td")[9].text.strip()
            + '", "required_stats": "' + driver.find_elements_by_tag_name("td")[11].text.strip().replace("\n", " ")
            + '", "damage": "' + driver.find_elements_by_tag_name("td")[13].text.strip()
            + '", "description": "' + driver.find_elements_by_tag_name("td")[15].text.strip().replace("\n", " ")
            + '", "dropped_by": ' + get_dropped_by(driver)
            +  ', "obtained_from": ' + get_obtained_from(driver)
            +  ', "note": "' + driver.find_elements_by_tag_name("td")[7].text.replace('"', '\\"')
            + '" },'
        )
    except:
        print("")

def get_dropped_by(driver):
    drops_str = ''
    drops = driver.find_elements_by_tag_name("td")[17].find_elements_by_tag_name("a")
    for drop in drops:
        drop_id = drop.get_attribute("href").split("id=")[-1]
        drop_name = drop_name = drop.text.strip()
        if not drop_name:
            if drops_str:
                drops_str += ', '
            drop_name = drop.find_element_by_tag_name("img").get_attribute("title")
            drops_str += '{ "id": "%s", "name": "%s" }'%(drop_id, drop_name)
    return "[" + drops_str + "]"

def get_obtained_from(driver):
    drops_str = ''
    drops = driver.find_elements_by_tag_name("td")[19].find_elements_by_tag_name("a")
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
