from selenium import webdriver
import time

def fnal(driver):
    time.sleep(6)
    driver.find_element_by_class_name('bid.bid-button-b').click()
    time.sleep(6)
    driver.find_element_by_class_name('button.right-button.button-red').click()
    time.sleep(6)
    driver.find_element_by_xpath("//div[contains(text(),'12W')]").click()
    time.sleep(6)
    driver.find_element_by_class_name('pill').click()
    time.sleep(6)
    driver.find_element_by_class_name('button.right-button.button.button-green').click()
    time.sleep(6)
    driver.find_element_by_class_name('button.button-slim.button-block.button-dark-grey').click()

email_id='grayhathacks10@gmail.com'
passwd = 'gentlemen&c0.'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.block_third_party_cookies": False})
print(chrome_options.arguments)
#chrome_options.add_argument("javascript.enabled", True)
chrome_options.add_argument("--enable-javascript")
driver = webdriver.Chrome(executable_path=r"C:\Users\Rahul\PaidProjects\Stockx\chromedriver.exe",options=chrome_options)
driver.get('https://stockx.com/login')
time.sleep(6)
print(chrome_options.arguments)
mail = driver.find_element_by_name("email")
passw = driver.find_element_by_name("password")
mail.send_keys(email_id)
time.sleep(10)
passw.send_keys(passwd)
time.sleep(10)
driver.find_element_by_class_name("button.right-button.button-green").click()
time.sleep(6)
driver.get('https://stockx.com/air-jordan-1-retro-high-satin-black-toe-w')
time.sleep(6)
"""try:
    driver.find_element_by_class_name('recaptcha-checkbox.goog-inline-block.recaptcha-checkbox-unchecked.rc-anchor-checkbox').click()
except Exception as ex:
    print("GRROR\n")
    print(ex)
    try :
        driver.find_element_by_class_name('recaptcha-checkbox-border').click()
    except Exception as exx:
        print('ERROR2')
        print(ex)
    finally : 
        print("IN_FINAL")
        fnal(driver)
finally:
    print("OUT_FINAL")
    fnal(driver)    """
driver.find_element_by_class_name('bid.bid-button-b').click()
time.sleep(6)
driver.find_element_by_class_name('button.right-button.button-red').click()
time.sleep(6)
driver.find_element_by_xpath("//div[contains(text(),'12W')]").click()
time.sleep(6)
driver.find_element_by_class_name('pill').click()
time.sleep(6)
driver.find_element_by_class_name('button.right-button.button.button-green').click()
time.sleep(6)
driver.find_element_by_class_name('button.button-slim.button-block.button-dark-grey').click()