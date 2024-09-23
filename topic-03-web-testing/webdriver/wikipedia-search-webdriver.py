from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


def test_inventor(invention, inventor):
    browser = webdriver.Firefox()
    browser.get(f"https://www.wikipedia.org/")
    assert "Wikipedia" in browser.title
    search_element = browser.find_element(by=By.ID, value="searchInput")
    search_element.send_keys(invention)
    # seach_element.send_keys(keys.RETURN)
    search_button = browser.find_element(
        by=By.CLASS_NAME, valeu="pure-button-primary-progressive"
    )
    search_button.click()
    sleep(2)
    assert (
        inventor in browser.page_source
    ), f"{inventor} is not listed as an inventor for {invention}"
    browser.close()


if __name__ == "__main__":
    test_inventor("Telephone", "Alexander Graham Bell")
    test_inventor("Transistor", "Bardeen")
    test_inventor("Light Bulb", "Edison")
    print("done.")
