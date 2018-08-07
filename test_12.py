import pytest
from selenium import webdriver
import os

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_add_new_product(driver):
    #переход на главную
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_xpath("//*[@id='box-login']/form/div[1]/table/tbody/tr[1]/td[2]/span/input").send_keys("admin")
    driver.find_element_by_xpath("//*[@id='box-login']/form/div[1]/table/tbody/tr[2]/td[2]/span/input").send_keys("admin")
    driver.find_element_by_xpath("//*[@id='box-login']/form/div[2]/button").click()

    #подсчёт количества продуктов в таблице
    count_product_old = count_of_products(driver)

    #Add New Product
    driver.find_element_by_xpath("//ul[@id='box-apps-menu']/li[2]/a/span[2]").click()
    driver.find_element_by_xpath("//*[@id='content']/div[1]/a[2]").click()

    #вкладка General
    driver.find_element_by_xpath("//a[contains(text(),'General')]").click()
    driver.find_element_by_xpath("//*[@id='tab-general']/table/tbody/tr[2]/td/span/input").send_keys("New duck")
    driver.find_element_by_xpath("//*[@id='tab-general']/table/tbody/tr[3]/td/input").send_keys("00123")
    driver.find_element_by_xpath("//*[@id='tab-general']/table/tbody/tr[7]/td/div/table/tbody/tr[2]/td[1]/input").click()
    driver.find_element_by_xpath("//*[@id='tab-general']/table/tbody/tr[8]/td/table/tbody/tr/td[1]/input").send_keys("100")
    path = os.path.join(os.path.dirname(__file__))
    driver.find_element_by_css_selector("input[type='file'][name='new_images[]']").send_keys(path + "\\123.jpg")
    driver.execute_script('$("%s").val(\'%s\')' % ("input[type='date'][name='date_valid_from']", "2018-08-06"))
    driver.execute_script('$("%s").val(\'%s\')' % ("input[type='date'][name='date_valid_to']", "2018-08-06"))

    #вкладка Information
    driver.find_element_by_xpath("//div[@class='tabs']/ul/li[2]/a[contains(text(),'Information')]").click()
    driver.find_element_by_xpath("//*[@id='tab-information']/table/tbody/tr[1]/td/select").click()
    driver.find_element_by_xpath("//*[@id='tab-information']/table/tbody/tr[1]/td/select/option[2]").click()
    driver.find_element_by_xpath("//*[@id='tab-information']/table/tbody/tr[3]/td/input").send_keys("Word123")
    driver.find_element_by_xpath("//*[@id='tab-information']/table/tbody/tr[5]/td/span/div/div[2]").send_keys("Desc")

    #вкладка Prices
    driver.find_element_by_xpath("//a[contains(text(),'Prices')]").click()
    driver.find_element_by_xpath("//*[@id='tab-prices']/table[1]/tbody/tr/td/input").send_keys("100")
    driver.find_element_by_xpath("//*[@id='tab-prices']/table[1]/tbody/tr/td/select").click()
    driver.find_element_by_xpath("//*[@id='tab-prices']/table[1]/tbody/tr/td/select/option[2]").click()

    #Save
    driver.find_element_by_xpath("//*[@id='content']/form/p/span/button[1]").click()

    #подсчёт количества продуктов в таблице после добавления товара
    count_product_new = count_of_products(driver)

    #проверка успешности добавления нового товара
    if (count_product_new - count_product_old) == 1:
        print("Product added success")
    else:
        print("Error")


#метод для подсчёта количества продуктов в таблице товаров
def count_of_products(driver):
    driver.find_element_by_xpath("//div[@id='box-apps-menu-wrapper']/ul/li[2]/a/span[@class='name']").click()
    products = driver.find_element_by_xpath("//*[@id='content']/form/table")
    products_list = products.find_elements_by_xpath("//*[@id='content']/form/table/tbody/tr[@class='row']")
    products_list_semi = products.find_elements_by_xpath("//*[@id='content']/form/table/tbody/tr[@class='row semi-transparent']")
    count_product = len(products_list) + len(products_list_semi)
    return count_product

