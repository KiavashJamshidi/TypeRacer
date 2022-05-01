from turtle import goto
from venv import main
from selenium import webdriver
from time import sleep

def goToSite(driver):
    driver.maximize_window()
    driver.get("https://play.typeracer.com/")

def waitToAgreeAndClickAgree(sec, driver):
    for i in range(sec):
        print("wainting to click on agree", sec - i, "seconds")
    driver.find_element_by_xpath("""//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]""").click()

def waitAndJoinRace(sec, driver):
    for i in range(sec):
        print("wainting to join race in", sec - i, "seconds")
        sleep(1)
    driver.find_element_by_xpath("""//*[@id="gwt-uid-1"]/a""").click()

def getWholeText(driver):
    a = driver.find_element_by_xpath("""//*[@id="nhwMiddlegwt-uid-11"]""").text
    b = driver.find_element_by_xpath("""//*[@id="nhwMiddleCommagwt-uid-12"]""").text
    c = driver.find_element_by_xpath("""//*[@id="nhwRightgwt-uid-13"]""").text
    wholeText = a + b + " " + c
    wholeText = wholeText.split(" ")
    sleep(1)
    return wholeText

def typeWords(driver, wholeText):
    for word in wholeText:
        driver.find_element_by_class_name("txtInput").send_keys(word + " ")
        sleep(0.07)

def waitToType(driver):
    while 1:
        remainTime = driver.find_element_by_xpath("""/html/body/div[4]/div/table/tbody/tr/td/table/tbody/tr/td[3]/div/span""").text.split(":")
        if len(remainTime) > 1:
            remainTime = remainTime[1]
        print(remainTime)
        if remainTime == '00':
            sleep(0.05)
            break

if __name__ == "__main__":
    driver = webdriver.Chrome("""G:\program files\chromedriver.exe""")
    goToSite(driver)
    # waitToAgreeAndClickAgree(3, driver)
    waitAndJoinRace(2, driver)

    sleep(2)
    
    waitToType(driver)
    wholeText = getWholeText(driver)
    typeWords(driver, wholeText)