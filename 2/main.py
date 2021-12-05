import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

browser = webdriver.Chrome(service=Service(f"{os.path.abspath(os.getcwd())}/chromedriver"))

logger.info('Wchodzę na zalando.pl')

browser.get('https://www.zalando.pl/')

temp = browser.find_element(By.CLASS_NAME, 'z-navicat-header_navToolItemLink')
temp.click()
logger.info('Wchodzę na stronę logowania')

time.sleep(2)

logger.info('Wpisuję login i hasło')

login = browser.find_element(By.XPATH, "//input[@id='login.email']")
login.send_keys('login')

login_button = browser.find_element(By.XPATH, "//button[@data-testid='login_button']")
login_button.click()

time.sleep(2)

logger.info('Pobieram błędy walidacji')
login_validation = browser.find_element(By.XPATH, "//span[contains(.,'Podaj pełny adres e-mail (np. jan.kowalski@domena.pl).')]")
password_validation = browser.find_element(By.XPATH, "//span[contains(.,'Pole obowiązkowe')]")

assert login_validation.text == "Podaj pełny adres e-mail (np. jan.kowalski@domena.pl)."
assert password_validation.text == "Pole obowiązkowe"

logger.info('poprawnie znalezione walidacje dla błędnego loginu i hasło')

browser.close()

loggerFirefox = logging.getLogger('logger-firefox')

loggerFirefox.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
loggerFirefox.addHandler(ch)

browser = webdriver.Firefox(service=Service(f"{os.path.abspath(os.getcwd())}/geckodriver"))

loggerFirefox.info('Wchodzę na stronę zalando.pl')

browser.get('https://www.zalando.pl/')

instagram = browser.find_element(By.XPATH, "//a[@aria-label='Instagram']")
facebook = browser.find_element(By.XPATH, "//a[@aria-label='Facebook']")

loggerFirefox.info('Pobieram linki do FB oraz IG')

instagram.get_attribute("href") == "https://www.instagram.com/zalando/"
facebook.get_attribute("href") == "https://www.facebook.com/zalando.polska"

loggerFirefox.info('Udało się znaleźć linki do FB oraz IG')

browser.close()