import pytest
from selenium import webdriver
import random

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_reg_and_login(driver):
    #переход на главную
    driver.get("http://localhost/litecart/en/")

    #регистрация нового пользователя
    registration = driver.find_element_by_xpath("//div[@id='box-account-login']/div/form/table/tbody/tr[5]/td/a")
    registration.click()

    #заполнение полей при регистрации
    driver.find_element_by_xpath("//*[@id='create-account']/div/form/table/tbody/tr[1]/td[1]/input").send_keys("123456")
    driver.find_element_by_xpath("//*[@id='create-account']/div/form/table/tbody/tr[1]/td[2]/input").send_keys("Komp")
    driver.find_element_by_xpath("//*[@id='create-account']/div/form/table/tbody/tr[2]/td[1]/input").send_keys("FName")
    driver.find_element_by_xpath("//*[@id='create-account']/div/form/table/tbody/tr[2]/td[2]/input").send_keys("LName")
    #выбор страны из выпадающего списка
    driver.find_element_by_xpath("//*[@id='create-account']/div/form/table/tbody/tr[5]/td[1]/span[2]/span[1]/span/span[2]/b").click()
    select_country = driver.find_element_by_xpath("/html/body/span/span/span[1]/input")
    select_country.send_keys("United States")
    select_country.send_keys(u'\ue007')
    #ввод адреса
    driver.find_element_by_xpath("//*[@id='create-account']/div/form/table/tbody/tr[3]/td[1]/input").send_keys("Address")
    driver.find_element_by_xpath("//*[@id='create-account']/div/form/table/tbody/tr[4]/td[1]/input").send_keys("19000")
    driver.find_element_by_xpath("//*[@id='create-account']/div/form/table/tbody/tr[4]/td[2]/input").send_keys("SPb")
    #рандомный адрес почты
    email = (''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(6)]))
    driver.find_element_by_xpath("//*[@id='create-account']/div/form/table/tbody/tr[6]/td[1]/input").send_keys(email)
    driver.find_element_by_xpath("//*[@id='create-account']/div/form/table/tbody/tr[6]/td[1]/input").send_keys("@ru.ru")
    #телефон и пароль
    driver.find_element_by_xpath("//*[@id='create-account']/div/form/table/tbody/tr[6]/td[2]/input").send_keys("+123456789")
    driver.find_element_by_xpath("//*[@id='create-account']/div/form/table/tbody/tr[8]/td[1]/input").send_keys("password")
    driver.find_element_by_xpath("//*[@id='create-account']/div/form/table/tbody/tr[8]/td[2]/input").send_keys("password")
    #клик креэйт аккаунт
    create_account = driver.find_element_by_xpath("//*[@id='create-account']/div/form/table/tbody/tr[9]/td/button").click()
    reg_success = driver.find_element_by_xpath("//*[@id='notices']/div")

    #логаут после регистрации
    driver.find_element_by_xpath("//*[@id='box-account']/div/ul/li[4]/a").click()
    driver.find_element_by_xpath("//*[@id='notices']/div")

    #лог ин
    driver.find_element_by_xpath("//*[@id='box-account-login']/div/form/table/tbody/tr[1]/td/input").send_keys("three@email.ru")
    driver.find_element_by_xpath("//*[@id='box-account-login']/div/form/table/tbody/tr[2]/td/input").send_keys("password")
    driver.find_element_by_xpath("//*[@id='box-account-login']/div/form/table/tbody/tr[4]/td/span/button[1]").click()

    #логаут после входа
    driver.find_element_by_xpath("//*[@id='box-account']/div/ul/li[4]/a").click()
    driver.find_element_by_xpath("//*[@id='notices']/div")