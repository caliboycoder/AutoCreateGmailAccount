from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import random
import time
import sys

class CreateGmail:
"""Auto Create Gmail Accounts with popular names"""

def __init__(self, firstname, lastname, username, pswd):
    self._firstname = firstname
    self._lastname = lastname
    self._username = username
    self._pswd = pswd
    self._Donefile = open("./data/CreatedAccounts.csv", "a")
    self.Initialize()

def Initialize(self):
    self._browser = webdriver.Chrome()
    self._browser.delete_all_cookies()
    self._browser.get("https://accounts.google.com/SignUp?hl=en")

def SetRecoveryEmail(self):
    CreatedEmails = pd.read_csv("./data/CreatedAccounts.csv")["username"].values
    if len(CreatedEmails) < 1:
        self.recovery_email = "pj.cs.vt@gmail.com"
    else:
        self.recovery_email = CreatedEmails[-1] + "@gmail.com"

def CreateAccount(self):
    # self.SetRecoveryEmail()
    self._browser.find_element_by_css_selector(r'input[id="firstName"]').send_keys(
        self._firstname
    )
    time.sleep(1)
    self._browser.find_element_by_css_selector(r'input[id="lastName"]').send_keys(
        self._lastname
    )
    time.sleep(1)
    self._browser.find_element_by_css_selector(r'input[id="username"]').send_keys(
        self._username
    )
    time.sleep(1)
    self._browser.find_element_by_css_selector(r'input[name="Passwd"]').send_keys(self._pswd)
    time.sleep(3 + 3 * random.random())
    self._browser.find_element_by_css_selector(r'input[name="ConfirmPasswd"]').send_keys(
        self._pswd
    )
    self._browser.find_element_by_css_selector(r'div[id="accountDetailsNext"]').click()
    self._browser.implicitly_wait(10)
    
    self._browser.find_element_by_css_selector('#phoneNumberId').send_keys("900000000") #replace with your ph no
    time.sleep(2)
    self._browser.find_element_by_css_selector('#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div.qhFLie > div > div > button > span').click()
    time.sleep(15)
    #self._browser.find_element_by_css_selector(r'div[id="view_container"]').click()
    #self._browser.implicitly_wait(10)
    #enter otp within 15 seconds and click on verify button all are automatic means what we do 
    self._browser.find_element_by_css_selector(
            "#month > option:nth-child(%d)" % random.randint(1, 13)
        ).click()
    self._browser.find_element_by_css_selector(r'#day').send_keys("25")
    time.sleep(2)
    self._browser.find_element_by_css_selector(r'#year').send_keys("1995")
    time.sleep(9)
    #Select Male Or Female which you needed that will not select automatically all are automatic means we are lazy so select 
    #and click next button ask for three times
    #dropdown = Select(driver.find_element_by_name("gender"))
    #dropdown.select_by_name("Male") 
    #self._browser.find_element_by_css_selector('#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div.qhFLie > div > div > button > div.VfPpkd-RLmnJb').click()
    #time.sleep(4) 
    #self._browser.find_element_by_css_selector('#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div.dG5hZc > div.daaWTb > div > div > button > span').click()
    #time.sleep(4)
    #self._browser.find_element_by_css_selector('#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div.qhFLie > div > div > button > div.VfPpkd-RLmnJb').click()
    time.sleep(30)

@staticmethod         
def GetUserInfo (firstnamefile, lastnamefile):
    FirstName = pd.read_csv(firstnamefile).sample(frac=1)
    LastName = pd.read_csv(lastnamefile).sample(frac=1)
    num = min(len(FirstName), len(LastName))
    if len(FirstName) > len(LastName):
       UserInfo = LastName
       UserInfo["firstname"] = FirstName.values[:num]
    else:
        UserInfo = FirstName
        UserInfo["lastname"] = LastName.values[:num]
    UserInfo.index = range(num)
    UserInfo.dropna()
    suffix = ""
    for i in range(6):
        suffix += str(random.randint(0, 9))
    UserInfo["username"] = UserInfo["firstname"] + UserInfo["lastname"] + suffix
    UserInfo["pswd"] = "super" + UserInfo["firstname"] + "233"
    return UserInfo

def   RunAppsScript(self, sharedlink):
    """So far, cannot auto totally
    
    Open sharedlink and then, plz manually finish Install. 
    """
    self._browser.get(sharedlink)
    time.sleep(10)
if name == "main":
SharedScript = "https://script.google.com/d/1yihwFAHrV17XHYmnrOJxQasqWGourSD57Xi-oFYO3sgY-B1_inPt5Vkc/edit?usp=sharing"

firstnamefile = "./data/CSV_Database_of_First_Names.csv"
lastnamefile = "./data/CSV_Database_of_Last_Names.csv"
UserInfoDF = CreateGmail.GetUserInfo(firstnamefile, lastnamefile)
for num in range(len(UserInfoDF)):
    UserInfoSeries = UserInfoDF.loc[num]
    CGM = CreateGmail(*UserInfoSeries)
    CGM.CreateAccount()
    # CGM.RunAppsScript(SharedScript)
    time.sleep(10)
