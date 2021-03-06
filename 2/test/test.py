import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
## ------------------------------------------------------------------------------------------------------------------
browser = webdriver.Chrome(service=Service(f"{os.path.abspath(os.getcwd())}/chromedriver"))

browser.get('https://www.zalando.pl/')
logger.info('Wchodzę na zalando.pl')

szukaj = browser.find_element(By.XPATH, "//input[@aria-label='Szukaj']")
logger.info('Szukam formularza wyszukiwania')

szukaj.send_keys("buty męskie zimowe")
szukaj.send_keys(Keys.RETURN)

logger.info('Szukam frazy "buty męskie zimowe"')

search_validation = browser.find_element(By.XPATH, "//span[contains(.,'Buty Męskie Zimowe')]")
assert search_validation.text == '‘Buty Męskie Zimowe ’'
logger.info('poprawnie znalezione wyszukiwane hasło na stronie')

browser.close()

## ------------------------------------------------------------------------------------------------------------------
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

## ------------------------------------------------------------------------------------------------------------------
browser = webdriver.Firefox(service=Service(f"{os.path.abspath(os.getcwd())}/geckodriver"))

loggerFirefox.info('Wchodzę na stronę zalando.pl w konkretny produkt')

browser.get('https://www.zalando.pl/tommy-hilfiger-casual-gloves-rekawiczki-pieciopalcowe-cognac-to152a022-o11.html')
dodaj = browser.find_element(By.XPATH, "//button[contains(., 'Dodaj do koszyka')]")
loggerFirefox.info('Dodaję do koszyka')
time.sleep(2)
dodaj.click()

browser.get('https://www.zalando.pl/cart/')
loggerFirefox.info('Przechodzę do koszyka')
time.sleep(2)
product = browser.find_element(By.LINK_TEXT, "Tommy Hilfiger")
assert product.get_attribute("href") == "https://www.zalando.pl/tommy-hilfiger-casual-gloves-rekawiczki-pieciopalcowe-cognac-to152a022-o11.html"
loggerFirefox.info('Produkt znaleziony w koszyku')

browser.close()
