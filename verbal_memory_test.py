import selenium;from bs4 import BeautifulSoup;import time;from selenium.webdriver.chrome.service import Service as ChromeService;from webdriver_manager.chrome import ChromeDriverManager;from selenium.webdriver.chrome.options import Options;import pyautogui;start_button = (796,947);new = (893,825);seen = (689,825);driver = selenium.webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()));url = 'https://humanbenchmark.com/tests/verbal-memory';driver.get(url);pyautogui.click(start_button);time.sleep(2);from selenium.webdriver.common.by import By;seen,new= driver.find_element(By.XPATH, "//button[text()='SEEN']"),driver.find_element(By.XPATH, "//button[text()='NEW']")
words = set() #making a set will mean lookup is faster probs... Also no duplicates and don'thave to run it twice to see if there are dupes 
x=500 #Value
def main():
    for _ in range(1,x+1):
        a().click()
def a():
    global words
    global new
    global seen
    if b() in words:
        return seen
    else:
        words.add(b())
        return new
def b():
    return BeautifulSoup(driver.page_source, 'html.parser').find('div', class_='word').text
if __name__ == '__main__':
    aa=time.time()
    print("Working")
    main()
    print(f"{time.time()-aa} Seconds")
time.sleep(1000)