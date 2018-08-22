from selenium import webdriver
from add_to_cart import AddToCart
from delete_from_cart import DeleteFromCart

class Application:

    def __init__(driver):
        driver.wd = webdriver.Chrome()
        driver.wd.implicitly_wait(5)
        driver.add_to_cart = AddToCart(driver)
        driver.delete_from_cart = DeleteFromCart(driver)

    def go_to_page(driver):
        wd = driver.wd
        wd.get("http://localhost/litecart/en/")

    def go_to_cart(driver):
        wd = driver.wd
        wd.find_element_by_xpath("//*[@id='cart']/a[3]").click()

    def destroy(driver):
        driver.wd.quit()