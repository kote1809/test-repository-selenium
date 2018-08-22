import pytest
from application import Application

@pytest.fixture
def driver(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_classes(driver):
    for n in range(3):
        driver.go_to_page()
        driver.add_to_cart.add()
    driver.go_to_cart()
    driver.delete_from_cart.delete()