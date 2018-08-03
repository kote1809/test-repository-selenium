import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_title_and_price(driver):
    print('Attention! Show started!')
    #переход на главную
    driver.get("http://localhost/litecart/en/")

    # название товара на главной странице
    first_element = driver.find_element_by_xpath("//div[@id='box-most-popular']/div/ul/li[1]/a[1]/div[1]/img")
    title_hp = first_element.get_attribute('alt')

    #получаем стикер элемента
    sticket_first_element = driver.find_element_by_xpath("//div[@id='box-most-popular']/div/ul/li[1]/a[1]/div[1]/div")
    sticker = sticket_first_element.get_attribute('textContent')

    #если элемент со стикером NEW, то у него только одна цена
    if sticker == 'New':
        print('Great choice! Your item from the collection <<NEW>>')
        #цена товара на главной странице
        first_element_price = driver.find_element_by_xpath("//div[@id='box-most-popular']/div/ul/li[1]/a[1]/div[4]/span")
        price_hp = first_element_price.get_attribute('textContent')
        #переход на страницу товара
        first_element.click()
        #название товара на странице товара
        first_element_page = driver.find_element_by_xpath("//div[@id='box-product']/div[1]/h1")
        title_ep = first_element_page.get_attribute('textContent')
        #цена товара на странице товара
        first_element_price_page = driver.find_element_by_xpath("//div[@id='box-product']/div[2]/div[2]/div[2]/span")
        price_ep = first_element_price_page.get_attribute('textContent')

        print('For title:')
        #сравнение названий на главной странице и на странице товара
        comparison_of_title(title_ep, title_hp)
        print('For price:')
        #сравнение цен на главной странице и на странице товара
        comparison_of_price(price_ep, price_hp)


    #иначе у него стикер SALE и у него будет старая и новая цены
    else:
        if sticker == 'Sale':
            print('Great choice! Your item from the collection <<SALE>>')
            #обычная цена на товаре с распродажи на главной странице
            first_element_old_price_hp = driver.find_element_by_xpath("//div[@id='box-most-popular']/div/ul/li[1]/a[1]/div[4]/s")
            price_old_hp = first_element_old_price_hp.get_attribute('textContent')
            colour_of_old_price_hp = first_element_old_price_hp.value_of_css_property('color')
            color_old_price_hp = pars_color(colour_of_old_price_hp)
            font_of_old_price_hp = first_element_old_price_hp.value_of_css_property('font-size')
            style_of_old_price_hp = first_element_old_price_hp.tag_name

            #цена со скидкой на главной странице
            first_element_new_price_hp = driver.find_element_by_xpath("//div[@id='box-most-popular']/div/ul/li[1]/a[1]/div[4]/strong")
            price_new_hp = first_element_new_price_hp.get_attribute('textContent')
            colour_of_new_price_hp = first_element_new_price_hp.value_of_css_property('color')
            color_new_price_hp = pars_color(colour_of_new_price_hp)
            font_of_new_price_hp = first_element_new_price_hp.value_of_css_property('font-size')
            style_of_new_price_hp = first_element_new_price_hp.tag_name

            #переход на страницу товара
            first_element.click()

            #название товара на странице товара
            first_element_page = driver.find_element_by_xpath("//div[@id='box-product']/div[1]/h1")
            title_ep = first_element_page.get_attribute('textContent')

            #обычная цена на товаре с распродажи на странице товара
            first_element_old_price_ep = driver.find_element_by_xpath("//div[@id='box-product']/div[2]/div[2]/div[2]/s")
            price_old_ep = first_element_old_price_ep.get_attribute('textContent')
            colour_of_old_price_ep = first_element_old_price_ep.value_of_css_property('color')
            color_old_price_ep = pars_color(colour_of_old_price_ep)
            font_of_old_price_ep = first_element_old_price_ep.value_of_css_property('font-size')

            #цена со скидкой на главной странице
            first_element_new_price_ep = driver.find_element_by_xpath("//div[@id='box-product']/div[2]/div[2]/div[2]/strong")
            price_new_ep = first_element_new_price_ep.get_attribute('textContent')
            colour_of_new_price_ep = first_element_new_price_ep.value_of_css_property('color')
            color_new_price_ep = pars_color(colour_of_new_price_ep)
            font_of_new_price_ep = first_element_new_price_ep.value_of_css_property('font-size')

        #проверки
            print('For title:')
            #сравнение названий на главной странице и на странице товара
            comparison_of_title(title_ep, title_hp)

            print('For OLD price:')
            #сравнение старой цены на главной странице с ценой на странице товара
            comparison_of_price(price_old_hp, price_old_ep)
            #сравнение размеров шрифтов старой и новой цен товара на главной странице
            comparison_of_font(font_of_old_price_hp, font_of_new_price_hp)
            #выяснение стиля старой цены
            comparison_of_style(style_of_old_price_hp)

            print('For NEW price:')
            #сравнение новой цены на главной странице с ценой на странице товара
            comparison_of_price(price_new_hp, price_new_ep)
            #сравнение размеров шрифтов старой и новой цен товара на странице товара
            comparison_of_font(font_of_old_price_ep, font_of_new_price_ep)
            #выяснение стиля новой цены
            comparison_of_style(style_of_new_price_hp)

            print('For home page:')
            #цвет старой цены на главной странице серый, а новой - красный?
            colour_is_grey(color_old_price_hp)
            colour_is_red(color_new_price_hp)

            print('For page element:')
            #цвет старой цены на странице продукта серый, а новой - красный?
            colour_is_grey(color_old_price_ep)
            colour_is_red(color_new_price_ep)



#методы

def comparison_of_style(style_of_price):
    if style_of_price == "s":
        print('OK: Style of old prise - crossed out')
    else:
        if style_of_price == "strong":
            print('OK: Style of new prise - fat')
        else:
            print('Error style')

def colour_is_red(color_two):
    if color_two[1] == color_two[2] == '0':
        print('OK: Colour of the price is RED')
    else:
        print('Error colour')

def colour_is_grey(color_one):
    if color_one[0] == color_one[1] == color_one[2]:
        print('OK: Colour of the price is GREY')
    else:
        print('Error colour')

def comparison_of_font(font_one, font_two):
    if font_one < font_two:
        print('OK: Font of the price of the goods is less than the font of the price with a discount')
    else:
        print('Error: Font of the price of the goods is greater than the font of the price with a discount')

def comparison_of_price(price_one, price_two):
    if price_one == price_two:
        print('OK: The price on the product page coincides with the name on the main page')
    else:
        print('Error price')

def comparison_of_title(title_ep, title_hp):
    if title_hp == title_ep:
        print('OK: The name on the product page coincides with the title on the main page')
    else:
        print('Error title')

def pars_color(str):
   rgb = []
   start = str.find("(")
   end = str.find(")")
   clr = str[start+1:end]
   rgb = clr.split(", ")
   return rgb








