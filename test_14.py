import pytest
from selenium import webdriver
import time

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

#проверка того, что ссылки рядом с новыми полями, имеют аттрибут таргет
def test_check_attribute(driver):
    #переход на главную
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_xpath("//*[@id='box-login']/form/div[1]/table/tbody/tr[1]/td[2]/span/input").send_keys("admin")
    driver.find_element_by_xpath("//*[@id='box-login']/form/div[1]/table/tbody/tr[2]/td[2]/span/input").send_keys("admin")
    driver.find_element_by_xpath("//*[@id='box-login']/form/div[2]/button").click()
    driver.find_element_by_xpath("//ul[@id='box-apps-menu']/li[3]").click()
    driver.find_element_by_xpath("//*[@id='content']/div/a").click()
    #ищем все элементы, у которых есть ссылка
    targets = driver.find_elements_by_xpath("//*[@id='content']/form/table[1]/tbody/tr/td/a")
    #сколько таких элементов найдено
    count = len(targets)
    #для каждого элемента проверим, что ссылка имеет атрибут таргет
    for i in range(count):
        targetElement = targets[i]
        target = targetElement.get_attribute("target")
        if target == "_blank":
            print("Link OK")
        else:
            ("Go to home")



#проверка открытия в новом окне
def test_open_new_window(driver):
    # переход на главную
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_xpath("//*[@id='box-login']/form/div[1]/table/tbody/tr[1]/td[2]/span/input").send_keys("admin")
    driver.find_element_by_xpath("//*[@id='box-login']/form/div[1]/table/tbody/tr[2]/td[2]/span/input").send_keys("admin")
    driver.find_element_by_xpath("//*[@id='box-login']/form/div[2]/button").click()
    driver.find_element_by_xpath("//ul[@id='box-apps-menu']/li[3]").click()
    driver.find_element_by_xpath("//*[@id='content']/div/a").click()
    #ищем все элементы, у которых есть ссылка
    targets = driver.find_elements_by_xpath("//*[@id='content']/form/table[1]/tbody/tr/td/a/i")
    #сколько таких элементов найдено
    count = len(targets)
    #для каждого элемента что-то сделаем
    for i in range(count):
        #посмотрим, сколько окон открыто
        handles_old = driver.window_handles
        count_handles_old = len(handles_old)
        #работаем с объектом i
        targetElement = targets[i]
        #открыли ссылку
        targetElement.click()
        # посмотрим, сколько окон стало
        handles_new = driver.window_handles
        count_handles_new = len(handles_new)
        #если прибавилось одно окно, продолжаем
        if (count_handles_new - count_handles_old) == 1:
            #делаем новое окно активным
            driver.switch_to_window(handles_new[1])
            #смотрим на него две секунды
            time.sleep(0.5)
            #закрываем это окно
            driver.close()
            #делаем активным предыдущее окно
            driver.switch_to_window(handles_new[0])
        #если вдруг открылось не одно окно или новое не открылось, то пишем ошибку
        else:
            print("UPS, Error")