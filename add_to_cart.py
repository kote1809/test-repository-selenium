import time

class AddToCart:

    def __init__(driver, app):
        driver.app = app

    def add(driver):
        wd = driver.app.wd
        cart_count = wd.find_element_by_xpath("//*[@id='cart']/a[2]/span[1]").text
        wd.find_element_by_xpath("//*[@id='box-most-popular']/div/ul/li[1]/a[1]/div[1]/img").click()
        colour_of_duck = wd.find_element_by_xpath("//*[@id='box-product']/div[1]/h1").get_attribute('textContent')
        if colour_of_duck == 'Yellow Duck':
            wd.find_element_by_xpath(
                "//*[@id='box-product']/div[2]/div[2]/div[5]/form/table/tbody/tr[1]/td/select").click()
            wd.find_element_by_xpath(
                "//*[@id='box-product']/div[2]/div[2]/div[5]/form/table/tbody/tr[1]/td/select/option[2]").click()
            wd.find_element_by_xpath(
                "//*[@id='box-product']/div[2]/div[2]/div[5]/form/table/tbody/tr/td/button").click()
        else:
            wd.find_element_by_xpath(
                "//*[@id='box-product']/div[2]/div[2]/div[5]/form/table/tbody/tr/td/button").click()
        time.sleep(2)
        cart_count_new = wd.find_element_by_xpath("//*[@id='cart']/a[2]/span[1]").get_attribute('textContent')
        if cart_count_new != cart_count:
            print("Add to cart success")
        else:
            print("Error")