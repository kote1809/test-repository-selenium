import time

class DeleteFromCart:

    def __init__(driver, app):
        driver.app = app

    def delete(driver):
        wd = driver.app.wd
        table = wd.find_element_by_xpath("//*[@id='order_confirmation-wrapper']/table")
        rows = table.find_elements_by_xpath("//tr/td[contains(@class,'item')]")
        count_rows_start = len(rows)
        print("Unique items in the cart:", + count_rows_start)

        while count_rows_start != 0:
            wd.find_element_by_xpath("//*[@id='box-checkout-cart']/div/ul/li[1]/form/div/p[4]/button").click()
            time.sleep(2)
            table = wd.find_element_by_xpath("//*[@id='order_confirmation-wrapper']/table")
            rows = table.find_elements_by_xpath("//tr/td[contains(@class,'item')]")
            count_rows_after_delete = len(rows)
            print("In the cart left:", + count_rows_after_delete)
            if (count_rows_start - count_rows_after_delete) == 1:
                print("Element was deleted")
                count_rows_start = count_rows_after_delete
                print("Unique items in the cart after deleted:", + count_rows_start)
                if count_rows_after_delete == 1:
                    wd.find_element_by_xpath(
                        "//*[@id='box-checkout-cart']/div/ul/li[1]/form/div/p[4]/button").click()
                    print("Element was deleted")
                    print("SUCCESS: Deleted all elements")
                    count_rows_after_delete = 0
                    count_rows_start = count_rows_after_delete
            else:
                print("Error deleted")

