import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
account = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/']")
account.click()
username = driver.find_element_by_id("username")
username.send_keys("st_helens@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("Aa2301887!#")
login = driver.find_element_by_css_selector("input[name='login']")
login.click()
shop = driver.find_element_by_xpath("//a[text()='Shop']")
shop.click()
forms = driver.find_element_by_css_selector("img[title='Mastering HTML5 Forms']")
forms.click()
driver.quit()


import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
account = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/']")
account.click()
username = driver.find_element_by_id("username")
username.send_keys("st_helens@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("Aa2301887!#")
login = driver.find_element_by_css_selector("input[name='login']")
login.click()
shop = driver.find_element_by_xpath("//a[text()='Shop']")
shop.click()
html = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/product-category/html/']")
html.click()
driver.quit()

from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
account = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/']")
account.click()
username = driver.find_element_by_id("username")
username.send_keys("st_helens@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("Aa2301887!#")
login = driver.find_element_by_css_selector("input[name='login']")
login.click()
shop = driver.find_element_by_xpath("//a[text()='Shop']")
shop.click()
sorting = driver.find_element_by_class_name("orderby")
sorting.click()
high_to_low = driver.find_element_by_css_selector("option[value='price-desc']")
high_to_low.click()
default = driver.find_element_by_css_selector("option[value='menu_order']")
default.click()
driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
account = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/']")
account.click()
username = driver.find_element_by_id("username")
username.send_keys("st_helens@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("Aa2301887!#")
login = driver.find_element_by_css_selector("input[name='login']")
login.click()
shop = driver.find_element_by_xpath("//a[text()='Shop']")
shop.click()
android = driver.find_element_by_css_selector("img[title='Android Quick Start Guide']")
android.click()
old_price = driver.find_element_by_css_selector(".price > del > span")
old_price_text = old_price.text
new_price = driver.find_element_by_css_selector(".price > ins > span")
new_price_text = new_price.text
assert old_price_text =="₹600.00"
assert new_price_text =="₹450.00"
book_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
book_cover.click()
book_cover_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
book_cover_close.click()
driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
shop = driver.find_element_by_xpath("//a[text()='Shop']")
shop.click()
basket = driver.find_element_by_css_selector("a[href='/shop/?add-to-cart=182']")
basket.click()
basket_in = driver.find_element_by_xpath("//span[text()='1 item']")
basket_in.click()
price_total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//span[text()='189.00']"), "₹189.00"))
driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
shop = driver.find_element_by_xpath("//a[text()='Shop']")
shop.click()
driver.execute_script("window.scrollBy(0,300);")
basket_html = driver.find_element_by_css_selector("a[href='/shop/?add-to-cart=182']")
basket_html.click()
time.sleep(5)
basket_js = driver.find_element_by_css_selector("a[href='/shop/?add-to-cart=180']")
basket_js.click()
basket_in = driver.find_element_by_class_name("cartcontents")
basket_in.click()
time.sleep(5)
del_first_book = driver.find_element_by_css_selector("a[data-product_id='182']")
del_first_book.click()
undo = driver.find_element_by_xpath("//a[text()='Undo?']")
undo.click()
step = driver.find_element_by_css_selector("input[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']").clear()
step = driver.find_element_by_css_selector("input[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
step.send_keys("3")
update_basket = driver.find_element_by_css_selector("input[name='update_cart']")
update_basket.click()
coupon = driver.find_element_by_css_selector("input[value='Apply Coupon']")
time.sleep(5)
coupon.click()
driver.quit()



import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
shop = driver.find_element_by_xpath("//a[text()='Shop']")
shop.click()
driver.execute_script("window.scrollBy(0,300);")
basket_html = driver.find_element_by_css_selector("a[href='/shop/?add-to-cart=182']")
basket_html.click()
basket_in = driver.find_element_by_xpath("//span[text()='1 item']")
basket_in.click()
checkout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='checkout-button button alt wc-forward']")))
checkout.click()
first_name = driver.find_element_by_id("billing_first_name")
first_name.send_keys("Alex")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Petrov")
email = driver.find_element_by_id("billing_email")
email.send_keys("asda@mail.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("1234567890")
sel = driver.find_element_by_css_selector("b[role='presentation']")
sel.click()
country = driver.find_element_by_id("s2id_autogen1_search")
country.send_keys("Russia")
country_in = driver.find_element_by_class_name("select2-match")
country_in.click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("lenina street")
city = driver.find_element_by_id("billing_city")
city.send_keys("la")
state = driver.find_element_by_id("billing_state")
state.send_keys("texas")
zip = driver.find_element_by_id("billing_postcode")
zip.send_keys("1234567")
driver.execute_script("window.scrollBy(0,600);")
time.sleep(5)
pay = driver.find_element_by_id("payment_method_cheque")
pay.click()
place = driver.find_element_by_id("place_order")
place.click()
thank_you = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
payment = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//td[text()='Check Payments']"), "Check Payments"))
driver.quit()
