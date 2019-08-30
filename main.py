from selenium import webdriver
email_id='grayhathacks10@gmail.com'
passwd = 'gentlemen&c0.'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.block_third_party_cookies": False})
print(chrome_options.arguments)
#chrome_options.add_argument("javascript.enabled", True)
chrome_options.add_argument("--enable-javascript")
driver = webdriver.Chrome(executable_path=r"C:\Users\Rahul\PaidProjects\Stockx\chromedriver.exe",options=chrome_options)
driver.get('https://stockx.com/login')
print(chrome_options.arguments)
mail = driver.find_element_by_name("email")
passw = driver.find_element_by_name("password")
mail.send_keys(email_id)
passw.send_keys(passwd)
driver.find_element_by_class_name("button.right-button.button-green").click()
driver.get('https://stockx.com/air-jordan-1-retro-high-satin-black-toe-w')
"""try:
    driver.find_element_by_class_name('recaptcha-checkbox.goog-inline-block.recaptcha-checkbox-unchecked.rc-anchor-checkbox').click()
except Exception as ex:
    print("GRROR\n")
    print(ex)
finally:"""
driver.find_element_by_class_name('button-container-b.bid-button.en-us').click()
driver.find_element_by_class_name('button.right-button.button-red').click()
driver.find_element_by_xpath("//div[contains(text(),'12W')]").click()
driver.find_element_by_class_name('pill').click()
driver.find_element_by_class_name('button.right-button.button.button-green').click()
driver.find_element_by_class_name('button.button-slim.button-block.button-dark-grey').click()
