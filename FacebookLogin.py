from selenium import webdriver
from time import sleep
browser = webdriver.Chrome(r"C:\Users\sgupta34\Desktop\ML\chromedriver_win32\chromedriver.exe")
browser.get('https://www.facebook.com/')

print ("Opened facebook")
sleep(1)

usr=input('Enter Email Id:')
pwd=input('Enter Password:')

username_box = browser.find_element_by_id('email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)

password_box = browser.find_element_by_id('pass')
password_box.send_keys(pwd)
print ("Password entered")

login_box = browser.find_element_by_id('loginbutton')
login_box.click()

print ("Done")
input('Press anything to quit')
browser.quit()
print("Finished")
