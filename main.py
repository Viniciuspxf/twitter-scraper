from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import pandas

import os

load_dotenv()

options = Options()
options.add_argument('--headless')
options.add_argument('--lang=en')

browser = webdriver.Chrome(options=options)
browser.get("https://twitter.com/")


loginButton = WebDriverWait(browser, timeout=5).until(
    lambda d: d.find_element(By.CSS_SELECTOR, "#layers > div > div:nth-child(1) > div > div > div > div > div > div > div > div:nth-child(1) > a > div"))
loginButton.click()


usernameField = WebDriverWait(browser, timeout=5).until(
    lambda d: d.find_element(By.CSS_SELECTOR, "input[autocomplete='username']"))
usernameField.send_keys(os.environ["EMAIL"])


nextButton = WebDriverWait(browser, timeout=5).until(
    lambda d: d.find_element(By.XPATH, "//span[contains(text(), 'Next')]"))
nextButton.click()

try:
    passwordField = WebDriverWait(browser, timeout=5).until(
        lambda d: d.find_element(By.CSS_SELECTOR, "input[autocomplete='current-password']"))
    passwordField.send_keys(os.environ["PASSWORD"])
except:
    phoneField = WebDriverWait(browser, timeout=5).until(
        lambda d: d.find_element(By.CSS_SELECTOR, "input[autocomplete='on']"))
    phoneField.send_keys(os.environ["PHONE"])

    nextButton = WebDriverWait(browser, timeout=5).until(
    lambda d: d.find_element(By.XPATH, "//span[contains(text(), 'Next')]"))
    nextButton.click()
finally:
    passwordField = WebDriverWait(browser, timeout=5).until(
        lambda d: d.find_element(By.CSS_SELECTOR, "input[autocomplete='current-password']"))
    passwordField.send_keys(os.environ["PASSWORD"])

    loginButton = WebDriverWait(browser, timeout=5).until(
    lambda d: d.find_elements(By.XPATH, "//span[contains(text(), 'Log in')]"))[1]

    loginButton.click()
    WebDriverWait(browser, timeout=5).until(
        lambda d: d.find_element(By.CSS_SELECTOR, "a[href='/home']")
    )

username= input("Digite o nome do usuário: ")
beginDate = input("Digite a data final no formato AAAA-MM-DD: ").strip()
endDate= input("Digite a data inical no formato AAAA-MM-DD: ").strip()
filename = input("Digite o nome do arquivo: ")
browser.get("https://twitter.com/")


browser.get("https://twitter.com/search?q=(from%3A"+ username + ")%20until%3A" + beginDate +"%20since%3A"+ endDate +"&src=typed_query&f=live")


tweets = WebDriverWait(browser, timeout=5).until(
        lambda d: d.find_element(By.CSS_SELECTOR, "article[data-testid='tweet']"))

dictOfTweets = dict()

previousHeight = -1
currentHeight = 0

while previousHeight != currentHeight:
    tweets = WebDriverWait(browser, timeout=5).until(
        lambda d: d.find_elements(By.CSS_SELECTOR, "article[data-testid='tweet']"))

    for tweet in tweets:
        datetime = tweet.find_element(By.CSS_SELECTOR, "time").get_attribute("datetime")
        textElement = tweet.find_element(By.CSS_SELECTOR, "div[data-testid='tweetText']")
        dictOfTweets[datetime] = textElement.text

    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.CONTROL, Keys.END)
    time.sleep(3)
    currentHeight, previousHeight = browser.execute_script("return document.body.scrollHeight"), currentHeight

dataframe = pandas.DataFrame.from_dict([dictOfTweets])
dataframe = dataframe.T
dataframe.to_excel(filename + ".xlsx")
print("FINALIZADO!")


