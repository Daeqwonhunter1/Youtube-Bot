from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

PATH = "/Users/dhunter/Desktop/chromedriver"


options = webdriver.ChromeOptions();
options.add_experimental_option("excludeSwitches", ['enable-automation']);
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(PATH,options=options)

class EmailLogin:
  def checkEmail(self):
    driver.get("https://mail.google.com/mail/u/1/#inbox")
    print("Gmail connected")
    self.LogIn()


  def LogIn(self):
    driver.find_element_by_id("identifierId").send_keys("selinapy2@gmail.com")
    driver.find_element_by_class_name("CwaK9").click()
    # driver.implicitly_wait(20)
    # driver.find_element_by_id("password").send_keys("102499Dq")
    # driver.find_element_by_class_name("U26fgb mUbCce fKz7Od YYBxpf PlRDoc M9Bg4d").click()
    # driver.find_element_by_css_selector()

    try:
      print("trying")
      
      WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[type=password")))
      print('Tried')
    finally:
      driver.find_element_by_class_name("Xb9hP").send_keys("102499Dq")
    print("Login")



class YoutubeLogin:
  def checkYoutube(self):
    driver.get('https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    print("Connected,Signing In")
    self.LoginEmail()


  def LoginEmail(self):
    try:
      driver.find_element_by_id("identifierId").send_keys("selinapy2@gmail.com")
    finally:
      driver.find_element_by_class_name("CwaK9").click()
      print("ConnectedEmail")
      self.LoginPassword()

  def LoginPassword(self):
    try:
      driver.implicitly_wait(10)
      print("waited")
    finally:
      driver.find_element_by_xpath('//span[@class="A37UZe sxyYjd MQL3Ob"]').click()
      print("clicked")
      driver.find_element_by_xpath('//input[@class="whsOnd zHQkBf"]').send_keys('102499Dq')
      driver.implicitly_wait(3)
      driver.find_element_by_xpath('//span[@class="CwaK9"]').click()


  def VideoClick(self):
    











login = YoutubeLogin()
login.checkYoutube()