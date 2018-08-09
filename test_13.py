import pytest
from selenium import webdriver
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

#в тесте добавляем N уточек в корзину с главной страницы
#затем удаляем их из корзины
def test_add_to_cart(driver):
    #добавить три товара с главной страницы в корзину
    for n in range(3):
        add_to_cart(driver)

    #переход в корзину
    driver.find_element_by_xpath("//*[@id='cart']/a[3]").click()

    #запомним, сколько уточек было в корзине до удаления
    count_rows_start = count_product_in_cart(driver)
    print("Unique items in the cart:", + count_rows_start)

    #по очереди будем удалять уточек, после каждого удаления проверка на count_rows
    #пока количество записей в таблице корзины не равно нулю выполняем удаление
    while count_rows_start != 0:
        #удаляем первый товар и делаем задержку для обновления таблицы
        driver.find_element_by_xpath("//*[@id='box-checkout-cart']/div/ul/li[1]/form/div/p[4]/button").click()
        time.sleep(2)
        #смотрим, сколько записей осталось в таблице корзины после удаления одной записи
        count_rows_after_delete = count_product_in_cart(driver)
        print("In the cart left:", + count_rows_after_delete)
        #если разница между тем, сколько записей было в таблице корзины, и тем, сколько записей осталось, равна 1, то удалён один товар и всё правильно
        if (count_rows_start - count_rows_after_delete) == 1:
            print("Element was deleted")
            #теперь количество записей в таблице корзины на 1 меньше после одного удаления
            count_rows_start = count_rows_after_delete
            print("Unique items in the cart after deleted:", + count_rows_start)
            #если после удаления в таблице корзины осталась всего одна запись, то после её удаления таблица исчезнет и проверять будет нечего
            #поэтому удаляем запись и обнуляем счётчики для выхода из цикла, так как все товары удалены
            if count_rows_after_delete == 1:
                driver.find_element_by_xpath("//*[@id='box-checkout-cart']/div/ul/li[1]/form/div/p[4]/button").click()
                print("Element was deleted")
                print("SUCCESS: Deleted all elements")
                count_rows_after_delete = 0
                count_rows_start = count_rows_after_delete
        #если произошла какая-то ошибка, выведем сообщение
        else:
            print("Error deleted")



#метод для подсчёта позиций в корзине
def count_product_in_cart(driver):
    table = driver.find_element_by_xpath("//*[@id='order_confirmation-wrapper']/table")
    rows = table.find_elements_by_xpath("//tr/td[contains(@class,'item')]")
    count_rows = len(rows)
    return count_rows

#метод добавления в корзину уточки
def add_to_cart(driver):
    # переход на главную
    driver.get("http://localhost/litecart/en/")
    # сколько продуктов в корзине сейчас, int
    cart_count = driver.find_element_by_xpath("//*[@id='cart']/a[2]/span[1]").text
    # переход на первый продукт
    driver.find_element_by_xpath("//*[@id='box-most-popular']/div/ul/li[1]/a[1]/div[1]/img").click()
    # если это жёлтая уточка, то надо выбрать размер
    colour_of_duck = driver.find_element_by_xpath("//*[@id='box-product']/div[1]/h1").get_attribute('textContent')
    if colour_of_duck == 'Yellow Duck':
        # выбираем размер
        driver.find_element_by_xpath(
            "//*[@id='box-product']/div[2]/div[2]/div[5]/form/table/tbody/tr[1]/td/select").click()
        driver.find_element_by_xpath(
            "//*[@id='box-product']/div[2]/div[2]/div[5]/form/table/tbody/tr[1]/td/select/option[2]").click()
        # и кликаем Add to Cart
        driver.find_element_by_xpath(
            "//*[@id='box-product']/div[2]/div[2]/div[5]/form/table/tbody/tr/td/button").click()
    else:
        # сразу кликаем Add to Cart
        driver.find_element_by_xpath(
            "//*[@id='box-product']/div[2]/div[2]/div[5]/form/table/tbody/tr/td/button").click()
    # подождём, пока корзина обновится
    time.sleep(3)
    # сколько стало продуктов в корзине после добавления
    cart_count_new = driver.find_element_by_xpath("//*[@id='cart']/a[2]/span[1]").get_attribute('textContent')
    # проверим, что корзина пополнилась
    if cart_count_new != cart_count:
        print("Add ro cart success")
    else:
        print("Error")

