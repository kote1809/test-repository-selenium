import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_menu(driver):
    #авторизация в админке
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("remember_me").click()
    driver.find_element_by_name("login").click()

    #поиск всех элементов основного меню
    menu = driver.find_elements_by_xpath("//ul[@id='box-apps-menu']//li[@id='app-']")
    #проходим по всем элементам меню, кликаем на каждый пункт и проверяем, что на загруженной странице есть заголовок (h1)
    for i in range(len(menu)):
        menu[i].click()
        h1 = driver.find_elements_by_xpath("//h1")
        if len(h1) == 0:
            print("Page hasn't elements h1")
        #проверяем, есть ли вложенные элементы у текущего пункта меню
        second = driver.find_elements_by_xpath("//li[@id='app-' and contains(@class, 'selected')]//li")
        if len(second) > 0:
            for k in range(len(second)):
                second[k].click()
                h1 = driver.find_elements_by_xpath("//h1")
                if len(h1) == 0:
                    print("Page hasn't elements h1")
                #переопределаем список вложенных элементов
                second = driver.find_elements_by_xpath("//li[@id='app-' and contains(@class, 'selected')]//li")
        #переопределаем список элементов основного меню
        menu = driver.find_elements_by_xpath("//ul[@id='box-apps-menu']//li[@id='app-']")