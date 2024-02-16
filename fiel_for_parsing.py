from time import sleep
from urllib.parse import unquote
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import pathes
from typing import Union
import json
import time 


TABLE = []


def get_element_text(driver: WebDriver, path: str) -> str:
    try:
        return driver.find_element(By.XPATH, path).text
    except NoSuchElementException:
        return ''

def move_to_element(driver: WebDriver, element: Union[WebElement, WebDriver]) -> None:
    try:
        webdriver.ActionChains(driver).move_to_element(element).perform()
    except StaleElementReferenceException:
        pass


def element_click(driver: Union[WebDriver, WebElement], path: str) -> bool:
    try:
        driver.find_element(By.XPATH, path).click()
        return True
    except:
        return False



def main():
    #Bishkek
    # url = 'https://2gis.kg/bishkek/search/Языковые%20школы/rubricId/675/filters/rating_rating_pretty_good'
    #Almaty
    url = 'https://2gis.kz/almaty/search/язфковые%20курсы/filters/rating_rating_perfect?m=77.068329%2C43.156125%2F10.32'
    #Astana
    # url = 'https://2gis.kz/astana/search/языковые%20курсы/filters/rating_rating_perfect'
    #Moscow
    # url = 'https://2gis.ru/moscow/search/Языковые%20школы/rubricId/675/filters/rating_rating_perfect'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    element_click(driver, pathes.main_banner)
    element_click(driver, pathes.cookie_banner)
    count_all_items = int(get_element_text(driver, pathes.items_count))
    pages = round(count_all_items / 12 + 0.5)
    for _ in range(pages):
        main_block = driver.find_element(By.XPATH, pathes.main_block)
        count_items = len(main_block.find_elements(By.XPATH, 'div'))
        for item in range(1, count_items + 1):
            if main_block.find_element(By.XPATH, f'div[{item}]').get_attribute('class'):
                continue
            item_clicked = element_click(main_block, f'div[{item}]/div/div[2]')
            if not item_clicked:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                element_click(main_block, f'div[{item}]/div/div[2]')
            time.sleep(1)
            title = get_element_text(driver, pathes.title)
            phone_btn_clicked = element_click(driver, pathes.phone_btn)
            phone = get_element_text(driver, pathes.phone) if phone_btn_clicked else ''
            move_to_element(driver, main_block)
            link = unquote(driver.current_url)
            address = get_element_text(driver, pathes.address)
            TABLE.append({
                'title':title,
                'phone':phone,
                'link':link,
                'address':address
            })
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element_click(driver, pathes.next_page_btn)
        sleep(0.5)
    driver.quit()
    
    with open('almaty.json', "w", encoding="utf-8") as json_file:
        json.dump(TABLE, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
    
    
























# from time import sleep
# from urllib.parse import unquote
# import pandas as pd
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.remote.webelement import WebElement
# import pathes
# from typing import Union
# import json
# import time 


# TABLE = []


# def get_element_text(driver: WebDriver, path: str) -> str:
#     try:
#         return driver.find_element(By.XPATH, path).text
#     except NoSuchElementException:
#         return ''

# def move_to_element(driver: WebDriver, element: Union[WebElement, WebDriver]) -> None:
#     try:
#         webdriver.ActionChains(driver).move_to_element(element).perform()
#     except StaleElementReferenceException:
#         pass


# def element_click(driver: Union[WebDriver, WebElement], path: str) -> bool:
#     try:
#         driver.find_element(By.XPATH, path).click()
#         return True
#     except:
#         return False



# def main():
#     #Bishkek
#     # url = 'https://2gis.kg/bishkek/search/Языковые%20школы/rubricId/675/filters/rating_rating_pretty_good'
#     #Almaty
#     url = 'https://2gis.kz/almaty/search/язфковые%20курсы/filters/rating_rating_perfect?m=77.068329%2C43.156125%2F10.32'
#     #Astana
#     # url = 'https://2gis.kz/astana/search/языковые%20курсы/filters/rating_rating_perfect'
#     #Moscow
#     # url = 'https://2gis.ru/moscow/search/Языковые%20школы/rubricId/675/filters/rating_rating_perfect'
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(url)
#     element_click(driver, pathes.main_banner)
#     element_click(driver, pathes.cookie_banner)
#     count_all_items = int(get_element_text(driver, pathes.items_count))
#     pages = round(count_all_items / 12 + 0.5)
#     for _ in range(pages):
#         main_block = driver.find_element(By.XPATH, pathes.main_block)
#         count_items = len(main_block.find_elements(By.XPATH, 'div'))
#         for item in range(1, count_items + 1):
#             if main_block.find_element(By.XPATH, f'div[{item}]').get_attribute('class'):
#                 continue
#             item_clicked = element_click(main_block, f'div[{item}]/div/div[2]')
#             if not item_clicked:
#                 driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#                 element_click(main_block, f'div[{item}]/div/div[2]')
#             time.sleep(1)
#             title = get_element_text(driver, pathes.title)
#             phone_btn_clicked = element_click(driver, pathes.phone_btn)
#             phone = get_element_text(driver, pathes.phone) if phone_btn_clicked else ''
#             move_to_element(driver, main_block)
#             link = unquote(driver.current_url)
#             address = get_element_text(driver, pathes.address)
#             TABLE.append({
#                 'title':title,
#                 'phone':phone,
#                 'link':link,
#                 'address':address
#             })
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         element_click(driver, pathes.next_page_btn)
#         sleep(0.5)
#     driver.quit()
    
#     with open('bishkek.json', "w", encoding="utf-8") as json_file:
#         json.dump(TABLE, json_file, ensure_ascii=False, indent=4)


# if __name__ == '__main__':
#     main()