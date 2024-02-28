from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
inp = input("what do u want to search for ")
PATH = r"D:\PROGRAMMING\selnium\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver.maximize_window()  # if need to maximise window
driver.get("https://www.pccasegear.com")
print(driver.title)

search = driver.find_element(
    by=By.XPATH, value='//*[@id="spotlight"]/div/div/div/form/input')
search.send_keys(inp)
search.send_keys(Keys.RETURN)
details = []

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ais-Hits"))
    )
    pages = main.find_element(
        by=By.XPATH, value='//*[@id="Algolia"]/div[2]/div[2]/div[1]/div[1]/span')
    pages = int(pages.text.split()[0])
    pages = pages//20
    print(pages)
    for page in range(pages+1):
        driver.implicitly_wait(2)
        items = main.find_elements(by=By.CLASS_NAME, value="ais-Hits-item")
        for item in items:
            price = item.text.split("\n")[3]
            name = item.text.split("\n")[0]
            detail = price + " " + name
            detail.strip()
            details.append(detail)
        try:
            next = driver.find_element(by=By.LINK_TEXT, value='›')
            driver.execute_script("arguments[0].click();", next)
        except:
            print("end of pages")

finally:
    driver.quit()
    # print(details)
    details.sort()
    # print(details)
    for aa in details:
        print(aa)
    #main = driver.find_element_by_class_name("ais-Hits")
