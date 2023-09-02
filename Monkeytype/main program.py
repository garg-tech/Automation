#importing all the modules
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time
import pymsgbox

url = 'https://monkeytype.com/'

browserOptions = webdriver.EdgeOptions()
browserOptions.add_experimental_option('detach', True)
browserOptions.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Edge(options = browserOptions)
browser.get(url) # to open monkeytype

browser.set_window_position(0, 0)
pyautogui.FAILSAFE = True #Failsafe mechanism
pyautogui.click(x=959, y=849) #accept cookies

delay = 0.000001
time.sleep(3)

#to allow the user to select different modes
pymsgbox.rootWindowPosition = "+1475+600"
pyautogui.alert(text = "Please select the mode and the time you want and then press Finish !", title = "Change settings", button = "Finish")

time.sleep(2)

#to type
try:
    #loop until there are no more active words remaining
    words = browser.find_elements(By.CLASS_NAME, "word")
    while len(words) != 0:
        active_word = browser.find_element(By.CSS_SELECTOR, ".word.active")
        letters = [letter.text for letter in active_word.find_elements(By.TAG_NAME, "letter")] + [' ']
        pyautogui.write(letters, interval=delay)
        words = browser.find_elements(By.CLASS_NAME, "word")
except Exception as e:
    pass

time.sleep(4)
pyautogui.screenshot("Typing Test Result.png") #to save test results
time.sleep(1)

browser.quit() #to close the browser
