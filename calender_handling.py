import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=opts)
# driver.implicitly_wait()

# driver.get('https://www.makemytrip.com/')
# time.sleep(4)
# driver.implicitly_wait(20)
#
# driver.find_element('xpath', '//span[text()="Departure"]').click()
# time.sleep(2)
#
# for i in range(1, 13):
#     month = driver.find_element('xpath', '//div[@class="DayPicker-Caption"]')
#     if month.text == 'December 2024':
#         driver.find_element('xpath', '//p[text()="14"]').click()
#         break
#     else:
#         driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()


#-------------------------------------------------------------------------------
## ALTERNATE SOLUTION
#
# driver.get('https://www.makemytrip.com/')
# time.sleep(4)
#
#
# driver.find_element('xpath', '//span[text()="Departure"]').click()
# time.sleep(2)
#
# for i in range(1, 13):
#     try:
#         driver.find_element('xpath', '//div[text()="December 2024"]/../..//p[text()="14"]').click()
#         break
#     except:
#         driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()


#---------------------------------------------------------------------------------------

## ASSIGNMENT
## 1. Go to goibibo.com and select the date
## 2. Go to  irctc and select the date
## 3. Go to booking.com and select the date
## 4. yatra
## 5. emirates

#----------------------------------------------------------------------------------------

## booking.com

# driver.get('https://www.booking.com/')
# time.sleep(5)
#
# driver.find_element('xpath', '//div[@data-testid="searchbox-dates-container"]').click()
# time.sleep(2)
#
# for i in range(1, 10):
#     try:
#         date = driver.find_element('xpath', '//span[@aria-label="17 July 2024"]')
#         date.click()
#         time.sleep(3)
#         driver.find_element('xpath', '//span[@aria-label="20 July 2024"]').click()
#         break
#     except:
#         driver.find_element('xpath', '//button[@aria-label="Next month"]').click()















































































